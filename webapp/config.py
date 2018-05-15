import os


class Config:
    SECRET_KEY = 'cd48e1c22de0961d5d1bfb14f8a66e006cfb1cfbf3f0c0f3'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 数据库配置
    DB_HOST = os.environ.get('DB_HOST', '127.0.0.1')
    DB_USER = os.environ.get('DB_USER')
    DB_PASS = os.environ.get('DB_PASS')
    DB_DATABASE = os.environ.get('DB_DATABASE')
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}/{database}'.format(
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        database=DB_DATABASE)
