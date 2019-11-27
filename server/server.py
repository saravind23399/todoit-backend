from flask import Flask
from flask_restplus import Api

# Import Configuration
import config

# Init Flask server
server = Flask(__name__)

# Application Configuration
server.config['SQLALCHEMY_DATABASE_URI'] = config.sqlalchemy.SQLALCHEMY_DATABASE_URI
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.sqlalchemy.SQLALCHEMY_TRACK_MODIFICATIONS

# Init Flask RestPlus API
api = Api(server, version='0.1', title='ToDoIt Backend', description='This is a Backend server written using Flask, Flask-RestPlus, SqlAlchemy')
