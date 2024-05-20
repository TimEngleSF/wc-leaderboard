from aiohttp import web
import aiohttp_jinja2
import jinja2

from settings import BASE_DIR
from handlers import index, get_leaderboard_page, get_leaderboard_time

app = web.Application()
app.router.add_static("/static/", path=str(BASE_DIR / "static"), name="static")
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(BASE_DIR / "templates")))
app.add_routes(
    [
        web.get("/", index),
        web.get("/leaderboard", get_leaderboard_page),
        web.get("/leaderboard/t/{page}", get_leaderboard_time),
    ]
)

if __name__ == "__main__":
    web.run_app(app)
