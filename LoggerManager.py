"""
Copyright 2006 VMware, Inc.  All rights reserved. -- VMware Confidential
"""
import logging
import logging.config
import os
import time


class Singleton(type):
    """
    The class defines the singleton mode logger for tool
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances.keys():
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class LoggerManager(object):
    __metaclass__ = Singleton
    _loggers = {}

    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def getLogger(name=None):
        default = "__app__"
        formatter = logging.Formatter('%(levelname)s: %(asctime)10s %(funcName)11s(%(lineno)d) -- %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')
        date_time = time.strftime("%d_%m_%Y")
        log_map = {"__main__": "FlightSchoolProject" + date_time + ".log",
                   "__twitter_trends_log__": "FlightSchoolProject" + date_time + ".log"}
        if name:
            logger = logging.getLogger(name)
        else:
            logger = logging.getLogger(default)

        # for writing into file
        handler = logging.FileHandler(os.path.join(os.path.join(os.getcwd(), 'Logs'), log_map[name]))
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        return logger
