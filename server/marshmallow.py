# Module Imports
from flask_marshmallow import Marshmallow

# Import Server
from .server import server

# Init Marshmallow
ma = Marshmallow(server)