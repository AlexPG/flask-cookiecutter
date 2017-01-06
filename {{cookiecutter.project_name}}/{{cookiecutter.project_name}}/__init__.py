from flask import Flask

from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
debug_toolbar = DebugToolbarExtension()
migrate = Migrate()

def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)
    debug_toolbar.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # Just for demo purposes
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    return app
