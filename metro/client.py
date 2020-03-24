from aiohttp import ClientSession, ClientTimeout
from metro.settings import Config


class HH:
    url_msk_metro = 'https://api.hh.ru/metro/1'
    timeout = Config.REQUEST_TIMEOUT

    @classmethod
    async def fetch_stations(cls):
        resp = await cls._get_json_response(cls.url_msk_metro)
        stations = await cls._get_stations_from_response(resp)
        return stations

    @classmethod
    async def _get_json_response(cls, url, timeout=None):
        timeout = timeout or cls.timeout
        timeout = ClientTimeout(timeout)
        async with ClientSession(raise_for_status=True) as session:
            async with session.get(url, timeout=timeout) as resp:
                response = await resp.json()
                return response

    @classmethod
    async def _get_stations_from_response(cls, metro_info):
        """Get stations list from HH response"""
        stations = []
        for line in metro_info['lines']:
            stations.extend([station['name'] for station in line['stations']])
        return stations
