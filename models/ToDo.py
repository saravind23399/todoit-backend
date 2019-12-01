from server import db
from sqlalchemy import ForeignKey

# Model - ToDo Item
class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key = True, )
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))
    created_by = db.Column(db.Integer, ForeignKey('users.id'))

    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description