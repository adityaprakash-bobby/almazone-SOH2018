from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config
from flask_googlemaps import GoogleMaps

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()
gmaps = GoogleMaps()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.app = app
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    gmaps.init_app(app)
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    from flaskblog.projects.routes import projects
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(projects)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
