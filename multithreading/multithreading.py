import time
import threading
import math
from threading import Thread

def runner(res_list, i, duration: float) -> None:
    time.sleep(duration)
    print(f"Successfully finished after {duration} seconds of sleeping")
    # return math.sin(duration)
    res_list[i] = math.sin(duration)

n = 1
thread_list = []
res_list = [None] * 10
i = 0
while n <= 10:
    t = Thread(target=runner, args=(res_list, i, n,))
    t.start()
    thread_list.append(t)
    n = n + 1
    i = i + 1

for th in thread_list:
    th.join()
print("Number of active threads is", threading.active_count())
print (res_list)
print("All threads are finished")
