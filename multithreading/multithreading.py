import time
import threading
import math
from threading import Thread 

def wrap_in_thread(function):
   
    def threading_decorator(*arg, **kwarg):

        t = Thread(target=function, args=arg, kwargs=kwarg)
        t.start()
        return t
   
    return threading_decorator

@wrap_in_thread
def runner(res_list, i, duration: float) -> None:
    time.sleep(duration)
    print(f"Successfully finished after {duration} seconds of sleeping")
    # return math.sin(duration)
    res_list[i] = math.sin(duration)

thread_list = []
res_list = [None] * 10
i = 0

for n in range(1, 11):
    t = runner(res_list, i, n)
    thread_list.append(t)
    i = i + 1

for th in thread_list:
    th.join()
print("Number of active threads is", threading.active_count())
print (res_list)
print("All threads are finished")
