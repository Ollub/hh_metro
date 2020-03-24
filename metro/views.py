from aiohttp import web
from metro.client import HH
from metro.helpers import compare_stations
from metro.logger import get_logger

logger = get_logger(__name__)

async def verify_stations(request):
    stations = await request.json()
    logger.info('Requested stations: {}'.format(stations))
    assert stations, 'Value of query parameter can not be empty'

    hh_stations = await HH.fetch_stations()
    diff = await compare_stations(stations, hh_stations,
                                  formatter=lambda x: x.lower().capitalize())
    return web.json_response(diff, status=200)
