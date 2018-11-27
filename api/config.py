import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig():
    SECRET_KEY = os.getenv('SECRET_KEY', 'test_with_barna'),
    DEBUG = False,

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    SECRET_KEY = 'my_prod_sec_key'
    DEBUG = True

class TestConfig(BaseConfig):
    DEBUG = True
