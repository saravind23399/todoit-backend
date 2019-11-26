from flask import Flask

# Import Configuration
import config

# Init Flask server
server = Flask(__name__)

# Application Configuration
server.config['SQLALCHEMY_DATABASE_URI'] = config.sqlalchemy.SQLALCHEMY_DATABASE_URI
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.sqlalchemy.SQLALCHEMY_TRACK_MODIFICATIONS
