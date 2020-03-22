from aiohttp import web
from routes import setup_routes
from middlewares import setup_middlewares

app = web.Application()
setup_routes(app)
setup_middlewares(app)
web.run_app(app)
