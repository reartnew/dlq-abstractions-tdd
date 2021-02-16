import time
import threading
import math
from threading import Thread 

class thread_extended(threading.Thread):
    
    def get_result(self):
        return res_list

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
    res_list[duration - 1] = math.sin(duration)

thread_list = []
res_list = [None] * 10

thread_list = [runner(i) for i in range(1,11)]

for th in thread_list:
    th.join()

print("Number of active threads is", threading.active_count())
print(thread_list[0].get_result())
print("All threads are finished")