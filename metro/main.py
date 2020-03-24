import os
from aiohttp import web
from metro.routes import setup_routes
from metro.middlewares import setup_middlewares
from metro.settings import Config

async def init_app():
    app = web.Application()
    app['config'] = Config
    setup_routes(app)
    setup_middlewares(app)
    return app

if __name__ == '__main__':
    app = init_app()
    web.run_app(init_app(), host='127.0.0.1', port=int(os.environ.get('SERVICE_PORT', 8080)))