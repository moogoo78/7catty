#import os

class Config(object):

    DEBUG = True
    SECRET_KEY = 'dev key'
    MEDIA_URL = 'media'

    NOTEBOOK_PATH = '/Users/moogoo/Dropbox/n/Notebook1'
    
class ProductionConfig(Config):
    DEVEL = False

class DevelConfig(Config):
    DEVEL = True
