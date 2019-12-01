import config
from server import server, api

# Import Models and Schemas
from models import ToDo
from schemas import todos_schema, todo_schema

# Import Routes
from routes import todosRoute, usersRoute

# Import Error Handlers
from routes import errorHandlers

# Register Error Handlers
server.register_blueprint(errorHandlers)

# Add Routes to API
api.add_namespace(todosRoute, path='/todos')
api.add_namespace(usersRoute, path='/users')

# Start Server
if __name__ == '__main__':
    server.run(port=3000, debug=config.debug)