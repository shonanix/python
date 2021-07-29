import time
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from server.optload import *
from server import optload
from dwebsocket.decorators import accept_websocket, require_websocket
from libs.websendmess import WebSendMessMix, WebReciveMessMix

# accept_websocket-—可以接受websocket请求和普通http请求
# require_websocket----只接受websocket请求,拒绝普通http请求
# Create your views here.


@accept_websocket
def syscontrol(request):
    # uesr_id = int(request.GET.get('uesrId'))
    uesr_id = "123Angd"
    if request.is_websocket():
        wb = WebSendMessMix()
        wr = WebReciveMessMix()
        # 当前任务不存在，即首次优化
        if not optload.Optimtask.__contains__(uesr_id):
            print_logging.info('优化服务启动，等待优化开始标志')
            wb.send_json_message(200, '优化服务启动，等待优化开始标志！', 1, 1, 1)
        while 1:
            uesr_id = "123Angd"
            jsonmessage = wr.receive_json_message()
            # if jsonmessage['status_code']:
            #     print(jsonmessage)
            # if jsonmessage:
            #     print(jsonmessage)
            # 算法开始标志
            if jsonmessage is not None and jsonmessage["status_code"] == 101:
                # 算法执行中
                if optload.Optimtask.__contains__(uesr_id):
                    wb.send_json_message(203, "优化服务已存在，成功获取", 1, 1, 1)
                    optim = optload.Optimtask[uesr_id]
                    # 算法正常运行中，继承当前进程
                    if optim.kt.is_alive():
                        optim.request = request
                    # 算法存在异常，重新启动算法
                    else:
                        optim.kt.kill()
                        optim = optload.Optimi(request)
                        optload.Optimtask[uesr_id] = optim
                        wb.send_json_message(200, '优化服务启动成功！', 1, 1, 1)
                        print_logging.info("优化服务启动成功!")
                        optim.main()
                # 启动优化算法
                else:
                    optim = optload.Optimi(request)
                    optload.Optimtask[uesr_id] = optim
                    wb.send_json_message(200, '优化服务启动成功！', 1, 1, 1)
                    print_logging.info("优化服务启动成功!")
                    optim.main()
            # 算法重连标志
            elif jsonmessage is not None and jsonmessage["status_code"] == 102:
                # 算法执行中
                if optload.Optimtask.__contains__(uesr_id):
                    wb.send_json_message(203, "优化服务已存在，成功获取", 1, 1, 1)
                    optim = optload.Optimtask[uesr_id]
                    # 算法正常运行中，继承当前进程
                    if optim.kt.is_alive():
                        optim.request = request
                    # 算法存在异常，重新启动算法
                    else:
                        optim.kt.kill()
                        optim = optload.Optimi(request)
                        optload.Optimtask[uesr_id] = optim
                        wb.send_json_message(200, '优化服务启动成功！', 1, 1, 1)
                        print_logging.info("优化服务启动成功!")
                        optim.main()
                else:
                    print_logging.info('优化服务启动，等待优化开始标志')
                    wb.send_json_message(200, '优化服务启动，等待优化开始标志！', 1, 1, 1)

            # 算法结束标志
            elif jsonmessage is not None and jsonmessage["status_code"] == 201:

                # 算法执行中
                if optload.Optimtask.__contains__(uesr_id):
                    optim = optload.Optimtask[uesr_id]
                    optload.Optimtask.pop(uesr_id)
                    # 关闭进程
                    optim.kt.kill()
                    optim.event.set()
                    print_logging.info('当前负荷优化服务已停止')
                    wb.send_json_message(203, '当前负荷优化服务已停止', 1, 1, 1)
            time.sleep(1)