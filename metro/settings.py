import os

class Config():
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    SERVICE_NAME = 'METRO'
    REQUEST_TIMEOUT = os.environ.get('REQUEST_TIMEOUT', 60)