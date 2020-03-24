from asyncio import coroutine
from metro.client import HH
from mock import Mock


hh_stations = ["Кунцевская", "Римская", "Стрешнево", "Раменки",
               "Китай-город", "Ясенево", "Сретенский бульвар"]
requested_stations = ["Кунцевская", "Римская", "Стрешнево", "Выхино"]

async def test_stations(client, hh_stations, req_stations):
    HH.fetch_stations = Mock(side_effect=coroutine(lambda: hh_stations))
    resp = await client.post('/api/v1/metro/verificate', json=req_stations)
    assert resp.status == 200
    res = await resp.json()
    assert res == {'unchanged': list(set(req_stations) & set(hh_stations)),
                    'updated': list(set(req_stations) - set(hh_stations)),
                    'deleted': list(set(hh_stations) - set(req_stations)),
                   }