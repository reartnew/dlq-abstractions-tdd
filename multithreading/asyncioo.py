import math
import asyncio

async def runner(duration: float) -> None:
    await asyncio.sleep(duration)
    print(f"Successfully finished after {duration} seconds of sleeping")
    return math.sin(duration)

async def main():
    tasks = []
    results_list = []
    for n in range(1,11):
        tasks.append(asyncio.create_task(runner(n)))
    for task in tasks:
        await task
        results_list.append(task.result())
    print(results_list)
    
asyncio.run(main())
