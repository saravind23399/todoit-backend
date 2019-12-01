from server import ma

# Schema - User
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'about')

# Init ToDo Schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)
