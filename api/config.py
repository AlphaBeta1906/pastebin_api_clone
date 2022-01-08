
class Config(object):
    import os
    from datetime import timedelta
    from dotenv import load_dotenv
    load_dotenv()
    

    basedir = os.path.abspath(os.path.dirname(__file__))

    DEBUG = True
    ENV = "development"
    SEND_FILE_MAX_AGE_DEFAULT = 0
    CACHE_DEFAULT_TIMEOUT = 3600
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_POOL_TIMEOUT = 86400
    SQLALCHEMY_POOL_SIZE = 200
    SQLALCHEMY_POOL_RECYCLE = 100
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SESSION_COOKIE_SECURE = True

class ConfigProd(Config):
    ENV = "production"
    DEBUG = False
    """
    SQLALCHEMY_DATABASE_URI = (
       "mysql+pymysql://pastebinCloneApi:farizi1234@pastebinCloneApi.mysql.pythonanywhere-services.com/pastebinCloneApi$pasteBin"
    )
    """

