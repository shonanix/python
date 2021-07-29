import json
import collections
from libs.middleware import GlobalRequestMiddleware

# 状态码类
Message_StateCode = collections.namedtuple('Message_StateCode', ['status_code', 'detail', "total_mode", "now_model", "groups"])


# websocket从前端接收消息
class WebReciveMessMix(object):

    def __init__(self, request=None):

        print('WebReciveMessMix')

        super().__init__()

        self.request = GlobalRequestMiddleware()

    # 非阻塞
    def receive_json_message(self) -> dict:

        if self.request is not None and self.request.is_websocket():
        # if self.request is not None and self.request.is_websocket() and self.request.websocket.has_messages():

            # 初始化message
            message = dict(Message_StateCode(None, None, None, None, None)._asdict())

            try:

                for json_message in self.request.websocket:

                    try:

                        message = json.loads(str(json_message, encoding='utf8'))

                    except:

                        pass

                    return message
            except:
                pass

    # 接收消息，收不到消息就阻塞
    def receive_json_message_wait(self) -> dict:

        if self.request is not None and self.request.is_websocket():

            # 初始化message
            message = dict(Message_StateCode(None, None, None, None, None)._asdict())
            # 外部再嵌套一个循环，不能是空的消息
            while True:

                json_message = self.request.websocket.wait()

                if json_message is not None:
                    break

            try:

                message = json.loads(str(json_message, encoding='utf8'))

            except:

                pass

            return message


# websocket向前端传消息
class WebSendMessMix(object):

    def __init__(self, request=None):

        print('in WebSendMessMix')

        super().__init__()

        self.request = GlobalRequestMiddleware()

    # 发送消息前检查获取的信息，是否webscoket关闭
    def send_message(self, message: str):

        if self.request is not None and self.request.is_websocket():

            self.request.websocket.send(bytes(message, encoding='utf8'))

    def send_json_message(self, code: int, detail: str, total_mode: int, now_model: int, groups: int):

        if self.request is not None:
            try:
                if self.request.is_websocket():

                    self.request.websocket.send(bytes(
                        json.dumps(dict(Message_StateCode(code, str(detail), total_mode, now_model, groups)._asdict()),
                                   ensure_ascii=False), encoding='utf8'))
            except:
                pass

    @staticmethod
    def send_message_decorator(message):

        if ('计算中' in message) == False:

            message = message + '，执行成功'

        def deco(func):

            def warp(self, *args, **kwargs):

                try:

                    fuc = func(self, *args, **kwargs)

                    if self.request.is_websocket():

                        self.request.websocket.send(bytes(message, encoding='utf8'))

                    return fuc

                except:

                    if self.request.is_websocket():
                        self.request.websocket.send(bytes(message + '，执行失败', encoding='utf8'))

            return warp

        return deco

