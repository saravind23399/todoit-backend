# Module Imports
from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


# Configuration
from config import sqlalchemy

# Init Flask server
server = Flask(__name__)

# Application Configuration
server.config['SQLALCHEMY_DATABASE_URI'] = sqlalchemy.SQLALCHEMY_DATABASE_URI
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = sqlalchemy.SQLALCHEMY_TRACK_MODIFICATIONS

# Init SQLAlchemy
db = SQLAlchemy(server)

# Init Marshmallow
ma = Marshmallow(server)

from models import ToDo
from schemas import todos_schema, todo_schema

# Root Route
@server.route('/', methods=['GET'])
def root():
    return jsonify({
        'msg': 'Hello World'
    })
    
# New ToDo Item
@server.route('/todos', methods=['POST'])
def createTodo():
    id = request.form['id']
    title = request.form['title']
    description = request.form['description']

    new_todo = ToDo(id, title, description)
    db.session.add(new_todo)
    db.session.commit()

    return todo_schema.jsonify(new_todo)

# Get all Todos
@server.route('/todos', methods=['GET'])
def allTodos():
    todos = ToDo.query.all()
    result = todos_schema.dump(todos)

    return jsonify(result)

# Get a single Todo
@server.route('/todos/<id>', methods=['GET'])
def getSingleTodo(id):
    todo = ToDo.query.get(id)
    return todo_schema.jsonify(todo)

# Update a Todo
@server.route('/todos/<id>', methods=['PUT'])
def updateTodo(id):
    todo = ToDo.query.get(id)

    title = request.form['title']
    description = request.form['description']

    todo.title = title
    todo.description = description

    db.session.commit()

    return todo_schema.jsonify(todo)

# Delete a single Todo
@server.route('/todos/<id>', methods=['DELETE'])
def deleteSingleTodo(id):
    todo = ToDo.query.get(id)

    db.session.delete(todo)
    db.session.commit()

    return todo_schema.jsonify(todo)
