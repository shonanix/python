from ctypes import *
import os
import json
import pandas as pd
from server.logger import Logger
logging = Logger(__file__).get_log()
def interface(request):

    if not request:
        msg = "请求信息为空，请检查格式消息"
        code = "400"
        result = {"msg": msg, "code": code}
        print("请求信息为空，请检查格式消息")
        return result

    try:
        dll = CDLL(os.path.join(os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'server'), 'dll'), 'libEngiDll.so'))
        dll.climateModel.argtypes = [c_char_p]
        dll.climateModel.restype = c_char_p
        arg = c_char_p(json.dumps(request).encode())
        logging.info(arg)
        result_json = dll.climateModel(arg)
        result_json = json.loads(result_json.decode())
        msg = "操作成功"
        code = "200"
        result = {"msg": msg, "code": code, "data": result_json}

    except Exception as e:
        logging.info(str(e))
        print(f'{e}')
        msg = "操作失败，" + str(e)
        code = "400"
        result = {"msg": msg, "code": code}

    print("解析已完成")
    return result


if __name__ == '__main__':
    interface([
    {
        "pid": 1,
        "part": 3,
        "aim_value": 50.0,
        "aim_type": 1,
        "control_mode": 1,
        "control_type": 1,
        "creator": 1
    },
    {
        "pid": 2,
        "part": 0,
        "aim_type": 6,
        "control_mode": 2,
        "control_type": 2,
        "creator": 1
    },
        {
            "pid": 3,
            "part": 0,
            "aim_type": 2,
            "aim_value": 50.0,
            "control_mode": 3,
            "control_type": 2,
        "creator": 1
        }
])
