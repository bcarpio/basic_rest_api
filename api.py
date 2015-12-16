from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}
class TodoSimple(Resource):
	def get(self, todo_id):
		print todo_id
 		return {todo_id: todos[todo_id]}


 	def put(self, todo_id):
 		todos[todo_id] = request.form['data']
 		return {todo_id: todos[todo_id]}

class GetTodos(Resource):
	def get(self):
		todo_list = todos
		return {'todo_list': todo_list}

api.add_resource(TodoSimple, '/<string:todo_id>')
api.add_resource(GetTodos, '/')

if __name__ == '__main__':
    app.run(debug=True)