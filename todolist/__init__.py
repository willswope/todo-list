from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_dance.contrib.google import make_google_blueprint, google

db = SQLAlchemy()


def create_app(test_mode=False):
    app = Flask(__name__)

    if test_mode:
        app.config.update(
            TESTING=True,
            SQLALCHEMY_DATABASE_URI='sqlite://',
            SQLALCHEMY_TRACK_MODIFICATIONS=False
        )
    else:
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite://',
            SQLALCHEMY_TRACK_MODIFICATIONS=False
        )

    app.config.from_pyfile('credentials.cfg')

    db.init_app(app)
    db.create_all(app=app)

    google_oauth_blueprint = make_google_blueprint(scope='openid email profile')
    app.register_blueprint(google_oauth_blueprint, url_prefix='/login')

    return app
