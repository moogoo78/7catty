import os

class Config(object):

    DEBUG = True
    SECRET_KEY = 'dev key'
    MEDIA_URL = 'media'

    #SRC_DIR = '/Users/moogoo/Dropbox/7catty'
    #SRC_DIR = '/home/sh/M/7catty'
    SRC_DIR = os.environ.get('SRC_DIR', '')
    EXCLUDE_DIR_LIST = ['__media']
    
class ProductionConfig(Config):
    DEVEL = False

class DevelConfig(Config):
    DEVEL = True
