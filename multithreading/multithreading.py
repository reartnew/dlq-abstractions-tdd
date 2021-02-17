import time
import threading
import math
from threading import Thread 
import typing

class thread_extended(threading.Thread):
    
    def __init__(self, target,
                 args, kwargs):
        self.__result = None

        def new_target(*argsx, **kwargsx):
            self.__result = target(*argsx, **kwargsx)
    
        super().__init__(target=new_target, args=args, kwargs=kwargs)

    def get_result(self):

        self.join()
        return self.__result

def wrap_in_thread(function):
   
    def threading_decorator(*arg, **kwarg):
        t = thread_extended(target=function, args=arg, kwargs=kwarg)
        t.start()
        return t
   
    return threading_decorator

@wrap_in_thread
def runner(duration: float) -> None:
    time.sleep(duration)
    print(f"Successfully finished after {duration} seconds of sleeping")
    return math.sin(duration)

thread_list = []

if __name__ == "__main__":

    thread_list = [runner(i) for i in range(1,11)]
    res_list = [thread.get_result() for thread in thread_list]

    print("Number of active threads is", threading.active_count())
    print(res_list)
    print("All threads are finished")