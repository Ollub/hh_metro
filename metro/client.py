from aiohttp import ClientSession, ClientTimeout


class HH:
    url_msk_metro = 'https://api.hh.ru/metro/1'

    @classmethod
    async def fetch_stations(cls):
        resp = await cls.__get_json_response(cls.url_msk_metro)
        stations = await cls.__get_stations_from_response(resp)
        return stations

    @classmethod
    async def __get_json_response(cls, url, timeout=60):
        timeout = ClientTimeout(timeout)
        async with ClientSession(raise_for_status=True) as session:
            async with session.get(url, timeout=timeout) as resp:
                response = await resp.json()
                return response

    @classmethod
    async def __get_stations_from_response(cls, metro_info):
        """Get stations list from HH response"""
        stations = []
        for line in metro_info['lines']:
            stations.extend([station['name'] for station in line['stations']])
        return stations
