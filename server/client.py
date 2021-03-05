import asyncio
import aiohttp

async def get(session):
    response = await session.get('http://0.0.0.0:80')
    tex = await response.text()
    status = response.status
    return (tex)

async def main():

    connect = aiohttp.BaseConnector(limit=10)
    async with aiohttp.ClientSession() as session:
        print(await asyncio.gather(*[get(session) for n in range(1,51)]))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
