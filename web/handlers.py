from aiohttp import web
import aiohttp
import aiohttp_jinja2
from dotenv import load_dotenv

import os

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")


@aiohttp_jinja2.template("content.html")
async def index(request):
    page = 1
    count = 10
    leaderboard_data = None
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"{API_BASE_URL}/top-xp?count={count}&page={page}"
        ) as response:
            leaderboard_data = await response.json()
    return {"leaderboard_data": leaderboard_data, "page": 1, "active_tab": "month"}


async def get_leaderboard_page(request):
    leaderboard_data = None
    count = request.query.get("count", 10)
    page = request.query.get("page", 2)
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"{API_BASE_URL}/top-xp?count={count}&page={page}"
        ) as response:
            leaderboard_data = await response.json()

    rendered_entries = [
        aiohttp_jinja2.render_string(
            "lb_entry.html",
            request,
            {"entry": entry, "page": int(page), "loop": {"index0": index}},
        )
        for index, entry in enumerate(leaderboard_data)
    ]

    rendered_leaderboard = "".join(rendered_entries)

    return web.Response(text=rendered_leaderboard, content_type="text/html")


@aiohttp_jinja2.template("tabs.html")
async def get_leaderboard_time(request):
    active_tab = request.match_info.get("page", "month")
    # leaderboard_data = None
    # async with aiohttp.ClientSession() as session:
    #     async with session.get(f"{API_BASE_URL}/top-xp?count=10&page=1") as response:
    #         leaderboard_data = await response.json()
    return {"active_tab": active_tab}
