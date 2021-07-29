from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from server.manualfunc import *
from server import manualfunc
import json
import time

@csrf_exempt
def primary(request):
    res = json.loads(request.body.decode())
    result = interface(res)
    return JsonResponse(result)


#
# def process_path():
#     if hasattr(sys, '_MEIPASS'):
#         ap = os.path.dirname(os.path.realpath(sys.executable))
#     else:
#         ap, filename = os.path.split(os.path.abspath(__file__))
#     return ap
#
# def process_ebsilon(request):
#
#     profile = request['profile']
#     modelname = request['modelname']
#     pp = process_path()
#     file_path = os.path.dirname(pp)
#     conf = 'config.ini'
#     config = configparser.ConfigParser()
#     config_path = os.path.join(os.path.join(file_path, "config"), 'config.ini')
#     try:
#         config.read('%s/%s' % (config_path, conf), encoding="utf-8-sig")
#     except:
#         raise FileExistsError('没有config配置文件')
#     version = config.get("profile", "version")
#     modelpath = os.path.join(file_path, modelname)
#     startapp()
#     get_all_objs()
#
# # open correct version of Ebsilon, open model, active profile
# def startapp():
#
#     # 打开ebsilon
#     pythoncom.CoInitialize()
#     application = Dispatch("EbsOpen.Application.Version." + version)  # open correct version of Ebsilon
#     model = application.ActiveModel
#     # if settings.calc_on_project.__contains__(task_id):
#     #     self.model = self.application.ActiveModel                               # open activemodel
#     # else:
#     #     self.model = self.application.Open(self.modelpath)                      # open model
#     activate(profile)  # active profile
#     oc = application.ObjectCaster  # the object caster
#     calculate()  # simulate the model
#
#     # quit the process
#
# def stopapp(self):
#
#     # 关闭ebsilon
#     stop = self.application.Process.Quit
#     del self.model
#     del self.oc
#     del self.application

    # result = runebsilon(json.loads(request.body.decode()))
    # return HttpResponse(json.dumps(result, indent=4, ensure_ascii=False))
