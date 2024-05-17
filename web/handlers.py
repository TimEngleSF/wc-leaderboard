from aiohttp import web
import aiohttp
import asyncio
import aiohttp_jinja2


@aiohttp_jinja2.template("leaderboard.html")
async def index(request):
    page = 1
    count = 10
    leaderboard_data = None
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"https://api.wordcraft.gg/api/top-xp?count={count}&page={page}"
        ) as response:
            leaderboard_data = await response.json()
            print(leaderboard_data)
    return {"leaderboard_data": leaderboard_data, "page": 1}
