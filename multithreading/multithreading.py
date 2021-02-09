import time
import threading
from threading import Thread

def runner(duration: float) -> None:
    time.sleep(duration)
    print(f"Successfully finished after {duration} seconds of sleeping")

n = 1
thread_list = []
while n <= 10:
    t = Thread(target=runner, args=(n,))
    t.start()
    thread_list.append(t)
    n = n + 1

for th in thread_list:
    th.join()
print("All threads are finished")