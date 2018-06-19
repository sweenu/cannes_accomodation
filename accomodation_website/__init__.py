from datetime import date

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


FESTIVAL_START = date(2018, 5, 8)
FESTIVAL_END = date(2018, 5, 19)

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__) 

    app.config.from_pyfile('config.py')

    db.init_app(app)

    from .views import bp
    app.register_blueprint(bp)
    
    login_manager.init_app(app)

    @app.shell_context_processor
    def shell_context():
        return {'app': app, 'db': db}

    return app
