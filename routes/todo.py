from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest
from services.todo_services import TodoServices
from services.user_services import UserServices
from tokens import validate_token
from schemas.validation import validate_json


todo = Blueprint('todo', __name__, url_prefix = '/todos')


@todo.route('/', methods = ['POST', 'GET'])
def create_or_get():
    if request.method == 'POST':
        header = request.headers.get('Authorization')

        if header is None:
            return jsonify({'message': 'Unauthorized'}), 401

        user_id = validate_token(header.split(' ')[1])

        print(id)

        if user_id is None:
            return jsonify({'message': 'Unauthorized'}), 401

        user_services = UserServices()

        user_exists = user_services.find_user_by_id(user_id)

        if not user_exists:
            return jsonify({'message': 'Unauthorized'}), 401

        if user_exists is None:
            return jsonify({'message': 'Internal server error'}), 500

        try:
            data = request.json
            validation = validate_json(data, 'Todo')
            if isinstance(validation, dict):
                return jsonify(validation), 400
        except BadRequest:
            return jsonify({'message': 'Invalid JSON format'}), 400

        title = data['title']
        description = data.get('description', "")

        todo_services = TodoServices()

        todo_id = todo_services.create_todo(title, description, user_id)

        return jsonify({'id': todo_id, 'title': title, 'description': description}), 200

        

        

        