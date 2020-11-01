# import flask - from the package import class
import os 
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

# create a function that creates a web application
# a web server will run this web application


def create_app():

    # this is the name of the module/package that is calling this app
    app = Flask(__name__)
    app.debug = True
    app.secret_key = 'utroutoru'
    # set the app configuration data
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketplace.sqlite'
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    # initialize db with flask app
    db.init_app(app)

    UPLOAD_FOLDER = 'auction\static\images'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    from auction import models

    bootstrap = Bootstrap(app)

    # initialize the login manager
    login_manager = LoginManager()

    # set the name of the login function that lets user login
    # in our case it is auth.login (blueprintname.viewfunction name)
    login_manager.login_view = 'auth.register'
    login_manager.init_app(app)

    # create a user loader function takes userid and returns User
    from .models import User  # importing here to avoid circular references

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.errorhandler(404)
    def not_found(e):
        return redirect(url_for('auth.error'))

    @app.errorhandler(401)
    def unauthorised(e):
        return redirect(url_for('auth.error'))

    @app.errorhandler(403)
    def forbidden(e):
        return redirect(url_for('auth.error'))

    @app.errorhandler(400)
    def not_retrievable(e):
        return redirect(url_for('auth.error'))

    @app.errorhandler(500)
    def server_error(e):
        return redirect(url_for('auth.error'))

    # importing views module here to avoid circular references
    # a commonly used practice.
    from . import views
    app.register_blueprint(views.bp)

    from . import auth
    app.register_blueprint(auth.bp)
    app.register_blueprint(auth.bp2)

    from . import items
    app.register_blueprint(items.bp)

    return app
