"""
Copyright 2006 VMware, Inc.  All rights reserved. -- VMware Confidential
This module will provide a singleton Logger, can log everything in the same app into one single log file.
"""
import logging
import logging.config
import os
import time
import constans


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
        # TODO: for different module, need to create new map item for logging
        log_map = {"__main__": constans.LOG_NAME_PRE + date_time + ".log",
                   "__twitter_trends_log__": constans.LOG_NAME_PRE + date_time + ".log"}
        if name:
            logger = logging.getLogger(name)
        else:
            logger = logging.getLogger(default)

        # for writing into file
        directory = os.path.join(os.getcwd(), 'Logs')
        # to check the log folder is existing or create a new one if necessary
        if not os.path.exists(directory):
            os.makedirs(directory)
        handler = logging.FileHandler(os.path.join(directory, log_map[name]))
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        return logger
