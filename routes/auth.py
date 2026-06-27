from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest
from schemas.validation import validate_json
from services.user_services import UserServices
from tokens import create_token


auth = Blueprint('users', __name__)


@auth.route('/register', methods = ['POST'])
def register():
    try:
        data = request.json
        validation = validate_json(data, 'Register')
        if isinstance(validation, dict):
            return jsonify(validation), 400
    except BadRequest:
        return jsonify({'message': 'Invalid JSON format'}), 400

    name = data['name']
    email = data['email']
    password = data['password']

    user_services = UserServices()

    email_exists = user_services.find_user_by_email(email)

    if email_exists is None:
        return jsonify({'message': 'Internal server error'}), 500

    if email_exists:
        return jsonify({'message': 'Email already registered'}), 409

    hashed_password = user_services.password_to_hash(password)

    user_id = user_services.add_user(name, email, hashed_password)

    if user_id is None:
        return jsonify({'message': 'Internal server error'}), 500

    return jsonify({'token': create_token(user_id)}), 200


@auth.route('/login', methods = ['POST'])
def login():
    try:
        data = request.json
        validation = validate_json(data, 'Login')
        if isinstance(validation, dict):
            return jsonify(validation), 400
    except BadRequest:
        return jsonify({'message': 'Invalid JSON format'}), 400
       
    email = data['email']
    password = data['password']

    user_services = UserServices()

    email_exists = user_services.find_user_by_email(email)

    if not email_exists:
        return jsonify({'message': 'Email or password are wrong'}), 401

    if email_exists is None:
        return jsonify({'message': 'Internal server error'}), 500

    db_user_id, db_password = user_services.get_id_and_password(email)

    is_valid = user_services.compare_passwords(db_password, password)

    if not is_valid:
        return jsonify({'message': 'Email or password are wrong'}), 401

    return jsonify({'token': create_token(db_user_id)}), 200

    

    