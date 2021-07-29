from libs.websendmess import WebSendMessMix, WebReciveMessMix

# 计时器
def count_time(sid):
    def deco_func(func):
        def wrapper(*args, **kwargs):
            if sid == "group":
                span = primaryNet.grouptimes
            elif sid == "batch":
                span = primaryNet.batchtimes
            else:
                span = primaryNet.alltimes
            t1 = time.time()
            fuc = func(*args, **kwargs)
            t2 = time.time()
            st = span - round(t2 - t1)
            if st > 0:
                print_logging.info(' %s 等待 %s s秒' % (func.__name__, st))
                time.sleep(st)
            return fuc
        return wrapper

    return deco_func


Optimtask = {}
class Optimi(WebSendMessMix, WebReciveMessMix):
    def __init__(self, request):
        self.request = request
        super(Optimi).__init__()
        self.event = threading.Event()
        
    @count_time("group")  
    def timescaleQuery(self, postQueryData):
        url_query = self.posturl
        try:
            r = requests.post(url_query, json=postQueryData)
            jsonResult = r.json()
            s = requests.Session()
            s.close()
        except:
            jsonResult = {'msg': '操作失败', 'code': '400', "data": {}}
        return jsonResult
      
      def get_token(self):

          headers = {"Content-Type": "application/json"}
          url = "http://%s:%s/auth/login" % (self.openip, self.tokenport)
          params = {"from": "saas", "password": "aaaaaa",
                    "projectName": "projectName", "username": "username"}
          result = requests.post(url, json=params, headers=headers)
          token = result.json().get('token')
        set_headers = {"Content-Type": "application/json", 'Authorization': "Bearer " + token}

        return set_headers
      
      def timescaleGet(self, control_id):
          headers = self.get_token()
          set_url = "http://%s:%s/minyong/controlCmd/send?controlId=%s" % (
                   self.openip, self.openport, control_id)
          res = requests.get(set_url, params=None, headers=headers)
          if "200" not in res.json().keys():
              logging.info(res.json())
