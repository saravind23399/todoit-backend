from server import db

# Model - ToDo Item
class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key = True, )
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))

    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description