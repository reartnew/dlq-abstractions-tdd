import time
import threading
from threading import Thread

def runner(duration: float) -> None:
    time.sleep(duration)
    print(f"Successfully finished after {duration} seconds of sleeping")

n = 1
while n <= 10:
    t = Thread(target=runner, args=(n,))
    t.start()
    n = n + 1
t.join()
print("All threads are finished")