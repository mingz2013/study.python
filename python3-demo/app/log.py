# -*- coding: utf-8 -*-
"""
@FileName: log
@Time: 2020/5/19 15:41
@Author: zhaojm

Module Description

"""

from datetime import datetime


# from app.config import config


def register_logging():
    import logging
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    from logging.handlers import RotatingFileHandler
    # 内部日志
    f = datetime.now().strftime('%Y-%m-%d')
    rotating_handler1 = RotatingFileHandler('logs/info-' + f + '.log', maxBytes=1 * 1024 * 1024 * 1024, backupCount=100)
    rotating_handler2 = RotatingFileHandler('logs/error-' + f + '.log', maxBytes=1 * 1024 * 1024 * 1024,
                                            backupCount=100)
    formatter1 = logging.Formatter(
        '%(asctime)s %(levelname)s - ''in %(funcName)s [%(filename)s:%(lineno)d]: %(message)s')
    rotating_handler1.setFormatter(formatter1)
    rotating_handler2.setFormatter(formatter1)
    logger = logging.getLogger('name')
    logger.addHandler(rotating_handler1)
    logger.addHandler(rotating_handler2)
    logger.setLevel(logging.INFO)
    rotating_handler2.setLevel(logging.ERROR)

    # if config.debug:
    # app.logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)

    return logger


logger = register_logging()


# def _logFunc(*argl, **argd):
#     # ftlog.xxx(... caller=self) for instance method
#     # ftlog.xxx(... caller=cls) for @classmethod
#     callerClsName = ""
#     try:
#         _caller = argd.get("caller", None)
#         if _caller:
#             if not hasattr(_caller, "__name__"):
#                 _caller = _caller.__class__
#             callerClsName = _caller.__name__
#             del argd["caller"]
#     except:
#         pass
#     if log_level > LOG_LEVEL_DEBUG:
#         print "[ ]",
#     else:
#         print "[" + callerClsName + "." + sys._getframe().f_back.f_back.f_code.co_name + "]",
#     return argd

def _log(*argl, **argd):
    _log_msg = ""
    for l in argl:
        if type(l) == tuple:
            ps = str(l)
        else:
            try:
                ps = "%r" % l
            except:
                try:
                    ps = str(l)
                except:
                    ps = 'ERROR LOG OBJECT'
        if type(l) == str:
            _log_msg += ps[1:-1] + ' '
        # elif type(l) == unicode:
        #     _log_msg += ps[2:-1] + ' '
        else:
            _log_msg += ps + ' '
    if len(argd) > 0:
        _log_msg += str(argd)

    # ct = datetime.now().strftime('%m-%d %H:%M:%S.%f')
    # _log_msg = ct + " " + _log_msg
    return _log_msg


def debug(*args, **kwargs):
    msg = _log(*args, **kwargs)
    logger.debug(msg)


def info(*args, **kwargs):
    msg = _log(*args, **kwargs)
    logger.info(msg)


def error(*args, **kwargs):
    msg = _log(*args, **kwargs)
    logger.error(msg)


def exception(*args, **kwargs):
    msg = _log(*args, **kwargs)
    logger.exception(msg)


def warn(*args, **kwargs):
    msg = _log(*args, **kwargs)
    logger.warn(msg)


def warning(*args, **kwargs):
    msg = _log(*args, **kwargs)
    logger.warning(msg)


def critical(*args, **kwargs):
    msg = _log(*args, **kwargs)
    logger.critical(msg)
