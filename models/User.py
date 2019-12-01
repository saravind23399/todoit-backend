from server import db

# Model - User Item
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, )
    username = db.Column(db.String(100))
    about = db.Column(db.String(100))

    def __init__(self, id, username, about):
        self.id = id
        self.username = username
        self.about = about