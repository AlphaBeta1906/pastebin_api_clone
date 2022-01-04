#!/usr/bin/env python


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
from flask_cors import CORS
from flask_marshmallow import Marshmallow

# app initiation
app = Flask(__name__)

db = SQLAlchemy(session_options={"autoflush": False})
migrate = Migrate()
app.config["CACHE_TYPE"] = "SimpleCache"
cache = Cache(app)
cors = CORS()
marshmallow = Marshmallow()

@app.errorhandler(404)
def _404(e):
    return {"message":"not found","code":404},404

@app.errorhandler(500)
def _500(e):
    return {"message":"internal server error","code":500},500

@app.errorhandler(400)
def _400(e):
    return  {"message":"one or some parameters not exsist","code":400},400

@app.errorhandler(403)
def _400(e):
    return  {"message":"authentication error","code":403},403

# TODO : fix blockquote
# TODO: add delete post(succes, just need to be better....kinda)

# note : email confirmation = email activation


def run():

    from .config import Config,ConfigProd
    
    # flask app factory
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    cache.init_app(app)
    cors.init_app(app)
    marshmallow.init_app(app)

    from .controller import paste

    from . import model
    # blueprint register
    url_prefix = "/api/v1"
    app.register_blueprint(paste, url_prefix=url_prefix)

    return app
