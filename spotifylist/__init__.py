from flask import Flask
from spotifylist.config import Config
from spotifylist.music.routes import music
from spotifylist.web.routes import web

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(music, url_prefix='/music')
    app.register_blueprint(web)

    return app
