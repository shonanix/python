import sys
import time
import threading


class KThread(threading.Thread):
    """A subclass of threading.Thread, with a kill()
    method.

    Come from:
    Kill a thread in Python:
    http://mail.python.org/pipermail/python-list/2004-May/260937.html
    """

    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.killed = False

    def start(self):
        """Start the thread."""
        self.__run_backup = self.run
        self.run = self.__run  # Force the Thread to install our trace.
        threading.Thread.start(self)

    def __run(self):
        """Hacked run function, which installs the
        trace."""
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, why, arg):
        if why == 'call':
            return self.localtrace
        else:
            return None

    def localtrace(self, frame, why, arg):
        if self.killed:
            if why == 'line':
                raise SystemExit()
        return self.localtrace

    def kill(self):
        self.killed = True

class  Fun():     
    def __init__(self, request):
        self.event = threading.Event()
    
    def func(self):
        
        for i in range(100):
            if self.event.is_set():
                break
            print(i)
            time.slpeep(1)
            
    def main(self):
        self.kt = KThread(target=self.func)
        self.kt.setDaemon(True)
        self.kt.start()
        
if __name__ == '__main__':
    demo = Fun()
    demo.main()
    i = 0
    while 1:
        if i >= 100:
            # 如果进程有阻塞则
            # demo.event.set()
            demo.kt.kill()
            print("强制结束子进程")
            break      
        if demo.kt.is_alive()        
            print("等待子进程结束中")
        else:
            break
        i = i + 1
        
