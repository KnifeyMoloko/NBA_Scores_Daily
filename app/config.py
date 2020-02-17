import os


class Config:
    SQLALCHEMY_DATABASE_URI = None
    table_names = []
    sslmode = None
    SECRET_KEY = 'Whatever'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    sslmode = 'require'


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')


config = {'production': ProductionConfig,
          'development': DevelopmentConfig,
          'testing': TestingConfig}
