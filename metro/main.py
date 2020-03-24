from aiohttp import web
from metro.routes import setup_routes
from metro.middlewares import setup_middlewares
from metro.settings import Config

app = web.Application()
setup_routes(app)
setup_middlewares(app)
app['config'] = Config
web.run_app(app)
