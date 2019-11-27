# Module Imports
from flask import Blueprint, jsonify, request, abort
from flask_restplus import Namespace, Resource

# Import Models and Schemas
from server import db
from models import ToDo
from schemas import todo_schema, todos_schema

todosRoute = Namespace('ToDo', description='These endpoints specify the CRUD Operations on Todo Items')

# ToDos Route Handler Class
@todosRoute.route('/')
class ToDos(Resource):
    def get(self):
        todos = ToDo.query.all()
        result = todos_schema.dump(todos)

        return jsonify(result)

    def post(self):
        id = request.form['id']
        title = request.form['title']
        description = request.form['description']

        new_todo = ToDo(id, title, description)
        db.session.add(new_todo)
        db.session.commit()

        return todo_schema.jsonify(new_todo)
    
# ToDo Route Handler Class
@todosRoute.route('/<int:id>')
class Todo(Resource):
    def get(self, id):
        todo = ToDo.query.get(id)

        if todo is None:
            abort(404, description= f"An Todo Item with the ID, '{id}' does not exist")

        return todo_schema.jsonify(todo)

    def put(self, id):
        todo = ToDo.query.get(id)

        title = request.form['title']
        description = request.form['description']

        todo.title = title
        todo.description = description

        db.session.commit()

        return todo_schema.jsonify(todo)

    def delete(self, id):
        todo = ToDo.query.get(id)

        db.session.delete(todo)
        db.session.commit()

        return todo_schema.jsonify(todo)
