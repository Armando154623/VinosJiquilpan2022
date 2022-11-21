class BaseConfig:
    DEBUG = True
    SECRET_KEY = "myKey"
    TESTING = True


class DevConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY = "myKey"
    TESTING = True


class ProdConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "myKey"
