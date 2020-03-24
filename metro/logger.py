import sys
import logging

from metro.settings import Config

common_log_level = logging.getLevelName(Config.LOG_LEVEL)


def stdout_handler():
    handler = logging.StreamHandler(sys.stdout)
    fmt = '%(asctime)s %(levelname)s %(message)s'
    handler.setFormatter(logging.Formatter(fmt))
    return handler


def get_logger(name=None, level=None, prefix=None):
    if name is None:
        name = Config.SERVICE_NAME
    logger = logging.getLogger(name)
    if level:
        if isinstance(level, str):
            level = logging.getLevelName(level)
    else:
        level = common_log_level
    logger.setLevel(level)
    if not logger.handlers:
        handler = stdout_handler()
        logger.addHandler(handler)
        if prefix:
            handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s {}: %(message)s'.format(prefix)))
    return logger
