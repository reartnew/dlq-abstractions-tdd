import time
import threading
import math
from threading import Thread 
from concurrent.futures import ThreadPoolExecutor, as_completed

def runner(duration: float) -> None:
    time.sleep(duration)
    print(f"Successfully finished after {duration} seconds of sleeping")
    return math.sin(duration)

thread_list = []
results_list = []
executor = ThreadPoolExecutor(10)
for n in range(1, 11):
    thread_list.append(executor.submit(runner, n))

for i in as_completed(thread_list):
    results_list.append(i.result())

print(results_list)