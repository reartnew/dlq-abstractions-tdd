import math
import asyncio

async def runner(duration: float) -> None:
    await asyncio.sleep(duration)
    print(f"Successfully finished after {duration} seconds of sleeping")
    return math.sin(duration)

async def main():
    print(await asyncio.gather(*[runner(n) for n in range(1, 11)]))
asyncio.run(main())
