from aiohttp import ClientSession, ClientTimeout

from metro.logger import get_logger
from metro.settings import Config


class HH:
    url_msk_metro = 'https://api.hh.ru/metro/1'
    timeout = Config.REQUEST_TIMEOUT
    cache = {}
    logger = get_logger(__name__)

    @classmethod
    async def fetch_stations(cls):
        resp_json = await cls._get_json_response(cls.url_msk_metro)
        stations = await cls._get_stations_from_response(resp_json)
        return stations

    @classmethod
    async def _get_json_response(cls, url, timeout=None):
        timeout = timeout or cls.timeout
        timeout = ClientTimeout(timeout)
        headers = {'If-None-Match': cls.cache.get('Etag', '')}
        async with ClientSession(raise_for_status=False) as session:
            async with session.get(url, headers=headers, timeout=timeout) as resp:
                cls.logger.info('Get response from HH API status={}'.format(resp.status))
                if resp.status == 304:
                    resp_json = cls.cache.get('resp_json')
                else:
                    cls.cache['Etag'] = resp.headers['Etag']
                    resp_json = await resp.json()
                    cls.cache['resp_json'] = resp_json
                return resp_json

    @classmethod
    async def _get_stations_from_response(cls, metro_info):
        """Get stations list from HH response"""
        stations = []
        for line in metro_info['lines']:
            stations.extend([station['name'] for station in line['stations']])
        return stations
