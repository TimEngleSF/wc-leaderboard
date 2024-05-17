from aiohttp import web
import aiohttp_jinja2
import jinja2

from routes import setup_routes
from settings import BASE_DIR
from handlers import index

app = web.Application()
app.router.add_static("/static/", path=str(BASE_DIR / "static"), name="static")
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(BASE_DIR / "templates")))
app.add_routes(
    [
        web.get("/", index),
    ]
)

if __name__ == "__main__":
    web.run_app(app)
