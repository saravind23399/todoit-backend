# Module Imports
from flask import Blueprint, jsonify, request, abort

# Import Models and Schemas
from server import db
from models import ToDo
from schemas import todo_schema, todos_schema

todosRoute = Blueprint('todos', __name__)
    
# New ToDo Item
@todosRoute.route('/todos', methods=['POST'])
def createTodo():
    id = request.form['id']
    title = request.form['title']
    description = request.form['description']

    new_todo = ToDo(id, title, description)
    db.session.add(new_todo)
    db.session.commit()

    return todo_schema.jsonify(new_todo)

# Get all Todos
@todosRoute.route('/todos', methods=['GET'])
def allTodos():
    todos = ToDo.query.all()
    result = todos_schema.dump(todos)

    return jsonify(result)

# Get a single Todo
@todosRoute.route('/todos/<id>', methods=['GET'])
def getSingleTodo(id):
    todo = ToDo.query.get(id)

    if todo is None:
        abort(404, description= f"An Todo Item with the ID, '{id}' does not exist")

    return todo_schema.jsonify(todo)

# Update a Todo
@todosRoute.route('/todos/<id>', methods=['PUT'])
def updateTodo(id):
    todo = ToDo.query.get(id)

    title = request.form['title']
    description = request.form['description']

    todo.title = title
    todo.description = description

    db.session.commit()

    return todo_schema.jsonify(todo)

# Delete a single Todo
@todosRoute.route('/todos/<id>', methods=['DELETE'])
def deleteSingleTodo(id):
    todo = ToDo.query.get(id)

    db.session.delete(todo)
    db.session.commit()

    return todo_schema.jsonify(todo)
