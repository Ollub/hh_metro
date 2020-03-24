from metro.views import verify_stations


def setup_routes(app):
    app.router.add_post('/api/v1/metro/verificate', verify_stations)
