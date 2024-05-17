from aiohttp import web


def setup_routes(app: web.Application):
    app.router.add_get("/", index)
