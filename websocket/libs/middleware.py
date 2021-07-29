from django.utils.deprecation import MiddlewareMixin


# 使得request变量全局化，直接实例化获取
class GlobalRequestMiddleware(MiddlewareMixin):

    __instance = None

    #
    def __new__(cls, *args, **kwargs):

        if not cls.__instance:

            cls.__instance = object.__new__(cls)

        return cls.__instance

    # 在view函数执行前先执行
    def process_request(self, request):

        GlobalRequestMiddleware.__instance = request