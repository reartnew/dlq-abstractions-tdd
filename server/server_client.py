import aiohttp
import asyncio
import random
from aiohttp import web

async def handle(request):
    await asyncio.sleep(random.randrange(3,5))
    return web.Response(text="It responds!")

async def get(session):
    response = await session.get('http://0.0.0.0:80')
    tex = await response.text()
    status = response.status
    return (tex)

async def main():

    loop = asyncio.get_event_loop()
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, port=80)
    await site.start()
    connect = aiohttp.TCPConnector(limit=10)
    async with aiohttp.ClientSession(connector=connect) as session:
        print(await asyncio.gather(*[get(session) for n in range(1,51)]))
    await runner.cleanup()

asyncio.run(main())
