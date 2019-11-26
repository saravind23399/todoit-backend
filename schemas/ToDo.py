from server import ma

# Schema - ToDo
class ToDoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description')

# Init ToDo Schema
todo_schema = ToDoSchema()
todos_schema = ToDoSchema(many=True)
