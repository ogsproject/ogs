import logging

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format = FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def warning(msg, *args, **kwargs):
    logger.warning(msg, *args, **kwargs)

def info(msg, *args, **kwargs):
    logger.info(msg, *args, **kwargs)

def debug(msg, *args, **kwargs):
    logger.debug(msg, *args, **kwargs)

def error(msg, *args, **kwargs):
    logger.error(msg, *args, **kwargs)
