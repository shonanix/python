import random
# from multiprocessing.dummy import Process as ThreadPool
from multiprocessing import Pool

if __name__ == '__main__':

    pool = Pool()
    for _ in range(2):
        pool.apply_async(func=job, args=(random.randint(1, 100), ))
    pool.close()
    # time.sleep(20)
    pool.join()


import threading
import requests
import time


class RequestThread(threading.Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.res = []

    def run(self):
        for _ in range(10):
            resp = requests.get(self.url)
            self.res.append(resp)


list_obj = []
st = time.time()
for _ in range(10):
    list_obj.append(RequestThread('http://httpbin.org/post'))
print('所有线程创建完毕：{}'.format(list_obj))
for obj in list_obj:
    obj.start()
for obj in list_obj:
    obj.join()
run_time = time.time() - st
print('总的耗时:{}s'.format(run_time))
print('平均每个请求所需要的时间:{}s'.format(run_time / 1000))
print([r.status_code for thread_obj in list_obj for r in thread_obj.res])

# 异步
import gevent
def job(i):
    print(i)
    gevent.sleep(2)
    return i
g= []
for _ in range(10):
    g.append(gevent.spawn(job, i=random.randint(2,100)))
st = time.time()
gevent.joinall(g)
print(time.time() - st)



import threading

class MyThread(threading.Thread):
    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)  # 在执行函数的同时，把结果赋值给result,
        # 然后通过get_result函数获取返回的结果

    def get_result(self):
        try:
            return self.result
        except Exception as e:
            return None
        
result = []
threads = []
t = MyThread(func1, args=(var))
t.start()
threads.append(t)
t = MyThread(func2, args=(var))
t.start()
threads.append(t)
for t in threads:
    t.join()  # 一定执行join,等待子进程执行结束，主进程再往下执行
    result.append(t.get_result())
