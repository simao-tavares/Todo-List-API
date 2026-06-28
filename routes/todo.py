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


@todo.route('/<int:id>', methods = ['PUT', 'DELETE'])
def update_or_delete(id):
    if request.method == 'PUT':
        header = request.headers.get('Authorization')

        if header is None:
            return jsonify({'message': 'Unauthorized'}), 401

        user_id = validate_token(header.split(' ')[1])

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

        todo_exists = todo_services.find_todo_by_id(id)

        if todo_exists is None:
            return jsonify({'message': 'Internal server error'}), 500

        if not todo_exists:
            return jsonify({'message': f'Task with id {id} not found'}), 404

        todo_user_id = todo_services.get_todo_userid(id)

        if int(user_id) != int(todo_user_id):
            return jsonify({'message': 'Forbidden'}), 403

        updated_title, updated_description = todo_services.update_todo(id, title, description)

        if updated_title is None or updated_description is None:
            return jsonify({'message': 'Internal server error'}), 500

        return jsonify({'id': id, 'title': updated_title, 'description': updated_description}), 200

    if request.method == 'DELETE':
        header = request.headers.get('Authorization')

        if header is None:
            return jsonify({'message': 'Unauthorized'}), 401

        user_id = validate_token(header.split(' ')[1])

        if user_id is None:
            return jsonify({'message': 'Unauthorized'}), 401

        user_services = UserServices()

        user_exists = user_services.find_user_by_id(user_id)

        if not user_exists:
            return jsonify({'message': 'Unauthorized'}), 401

        if user_exists is None:
            return jsonify({'message': 'Internal server error'}), 500
        
        todo_services = TodoServices()

        todo_exists = todo_services.find_todo_by_id(id)

        if todo_exists is None:
            return jsonify({'message': 'Internal server error'}), 500

        if not todo_exists:
            return jsonify({'message': f'Task with id {id} not found'}), 404

        todo_user_id = todo_services.get_todo_userid(id)

        if int(user_id) != int(todo_user_id):
            return jsonify({'message': 'Forbidden'}), 403

        delete_todo = todo_services.delete_todo(id)

        if delete_todo is None:
            return jsonify({'message': 'Internal server error'}), 500

        return '', 204
        

        