# Import flask and template operators
from flask import Flask, render_template, send_from_directory

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__, static_url_path='/static')

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (home)
from app.home.controllers import home as home
from app.api.controllers import api as api

# Register blueprint(s)
app.register_blueprint(home)
app.register_blueprint(api)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
