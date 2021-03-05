import aiohttp
import asyncio
import random
from aiohttp import web

async def handle(request):
    await asyncio.sleep(random.randrange(3,5))
    return web.Response(text="It responds!")

app = web.Application()
app.router.add_get('/', handle)
web.run_app(app, port=80)
