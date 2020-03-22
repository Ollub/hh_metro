import json
from aiohttp import web
from client import HH
from helpers import compare_stations


async def verify_stations(request):
    stations = request.query['stations']
    stations = json.loads(stations)
    hh_stations = await HH.fetch_stations()
    diff = await compare_stations(stations, hh_stations,
                                  formatter=lambda x: x.lower().capitalize())
    return web.json_response(diff, status=200)
