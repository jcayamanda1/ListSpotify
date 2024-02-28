from flask import Flask
from flask_dotenv import DotEnv

from yourproject.music.routes import music
from yourproject.web.routes import web

def create_app():
    app = Flask(__name__)
    
    # Load configuration from .env file or environment variables
    env = DotEnv(app)
    app.secret_key = app.config.get('SECRET_KEY')  # Loaded from .env or environment
    
    # Register Blueprints
    app.register_blueprint(music)
    app.register_blueprint(web)

    return app

# SECRET_KEY=your_secret_key_here

