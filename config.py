#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'daben_chen'
__version__ = "1.0.1"
__email__ = "vida112728@gmail.com"

class Config(object):
    """Base config class."""
    pass

class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Development config class."""
    # Open the DEBUG
    DEBUG = True
    BABEL_DEFAULT_LOCALE = 'zh_CN'
    SECRET_KEY = '1234567890'
    DATABASE_FILE = 'db.sqlite'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
