import config
from server import server

# Import Models and Schemas
from models import ToDo
from schemas import todos_schema, todo_schema

# Import Routes
from routes import todosRoute

# Import Error Handlers
from routes import errorHandlers

# Register Blueprints
server.register_blueprint(todosRoute)
server.register_blueprint(errorHandlers)


# Start Server
if __name__ == '__main__':
    server.run(port=3000, debug=config.debug)