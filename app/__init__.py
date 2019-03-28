import sys
import json
from flask import Flask
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


def getJSON(filename):
    try:
        with open(filename,'r') as fp:
            return json.load(fp)
    except FileNotFoundError:
        print("Couldn't find key, exiting the program...")
        sys.exit(1)


app = Flask(__name__)
app.config.from_json('keys.json')

keys = getJSON("keys.json")
MAIL_EMAIL = keys.get("MAIL_USERNAME")

db = SQLAlchemy()

bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()

from app.users.routes import users
from app.posts.routes import posts
from app.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)


def create_app(json_path="../keys.json"):
    app = Flask(__name__)
    app.config.from_json(json_path)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from app.users.routes import users
    from app.posts.routes import posts
    from app.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app
