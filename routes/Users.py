# Module Imports
from flask import Blueprint, jsonify, request, abort
from flask_restplus import Namespace, Resource
from sqlalchemy import exc

# Import Models and Schemas
from server import db
from models import User
from schemas import user_schema, users_schema

usersRoute = Namespace('Users', description='These endpoints specify the CRUD Operations on Users')

@usersRoute.route('')
class Users(Resource):
    def get(self):
        users = User.query.all()
        result = users_schema.dump(users)

        return jsonify(result)

    def post(self):
        id = request.form['id']
        username = request.form['username']
        about = request.form['about']

        try:
            new_user = User(id, username, about)
            
            db.session.add(new_user)
            db.session.commit()

        except exc.SQLAlchemyError:
            abort(400, f"An User with the ID, {id} already exists")

        return user_schema.jsonify(new_user)
        
@usersRoute.route('/<int:id>')
class User(Resource):
    def get(self, id):
        user = User.query.get(id)
        if user is None:
            abort(404, description=f"An User with the ID, {id} doesn't exist")

        return user_schema.jsonify(user)

    def put(self, id):
        user = User.query.get(id)
        if user is None:
            abort(404, description=f"An User with the ID, {id} doesn't exist")

        formData = request.form

        if 'username' in formData.keys():
            user.username = formData['username']

        if 'about' in formData.keys():
            user.about = formData['about']

        db.session.commit()

        return user_schema.jsonify(user)

    def delete(self, id):
        user = User.query.get(id)
        
        if user is None:
            abort(404, description=f"An User with the ID, {id} doesn't exist")

        db.session.delete(user)
        db.session.commit()

        return user_schema.jsonify(user)
