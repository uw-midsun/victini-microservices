from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .config import config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_mode):
    app = Flask(__name__)
    app.config.from_object(config[config_mode])

    db.init_app(app)
    migrate.init_app(app, db)

    return app

# After database has been defind in models.py, the create_app function should change to initialize the database
# def create_app(config_mode):
#     app = Flask(__name__)
#     app.config.from_object(config[config_mode])

#     db.init_app(app)
#     migrate.init_app(app, db)

#     with app.app_context():
#         db.create_all()

#     return app
