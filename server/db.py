# Module Imports
from flask_sqlalchemy import SQLAlchemy

# Import Server
from .server import server

# Init SQLAlchemy
db = SQLAlchemy(server)
