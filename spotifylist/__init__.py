from flask import Flask
from spotifylist.config import Config
from spotifylist.music.routes import music
from spotifylist.web.routes import web
from spotifylist.artist.routes import artist
from spotifylist.album.routes import album
from spotifylist.genre.routes import genre


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(music, url_prefix='/music')
    app.register_blueprint(artist, url_prefix='/artist') 
    app.register_blueprint(album, url_prefix='/album') 
    app.register_blueprint(genre, url_prefix='/genre') 

    app.register_blueprint(web)

    return app
