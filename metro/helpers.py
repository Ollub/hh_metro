async def compare_stations(requested, from_api, formatter=lambda x: x.lower()):
    if not formatter:
        requested = set(requested)
        from_api = set(from_api)
    else:
        requested = {formatter(elem) for elem in requested}
        from_api = {formatter(elem) for elem in from_api}
    return {
        'unchanged': list(requested & from_api),
        'updated': list(requested - from_api),
        'deleted': list(from_api - requested),
    }
