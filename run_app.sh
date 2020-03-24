#!/bin/bash

echo "~~~~~~~~~~ Starting REST server ~~~~~~~~~~"
exec gunicorn metro.main:init_app --config gunicorn_config.py --worker-class aiohttp.GunicornWebWorker
