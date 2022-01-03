class Config(object):
    import os
    from datetime import timedelta

    basedir = os.path.abspath(os.path.dirname(__file__))

    DEBUG = True
    ENV = "development"
    SECRET_KEY = "ER46324834YGguydgfY89ro4IUYT*d:sd34|dfy#$%"
    SECURITY_PASSWORD_SALT = "f8wetqw<tq&57g-78b6s6qarrt4Hy2&)12~~/82232e"
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SEND_FILE_MAX_AGE_DEFAULT = 0
    CACHE_DEFAULT_TIMEOUT = 3600
    
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:f%40r1Zi1906@localhost:3306/paste"
    )
    SQLALCHEMY_POOL_TIMEOUT = 86400
    SQLALCHEMY_POOL_SIZE = 200
    SQLALCHEMY_POOL_RECYCLE = 100
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SESSION_COOKIE_SECURE = True

class ConfigProd(Config):
    ENV = "production"
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = (
       "mysql+pymysql://pastebinCloneApi:farizi1234@pastebinCloneApi.mysql.pythonanywhere-services.com/pastebinCloneApi$pasteBin"
    )
    JWT_COOKIE_SECURE = True
