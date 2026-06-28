import json
from passwordlib.analyzer import Analyzer
from jsonschema import validate, FormatChecker, ValidationError


class WeakPassword(Exception):
    pass

    
def validate_json(json_data: dict, type_of_operation: str):
    if type_of_operation == 'Register':
        with open('schemas/auth/register.json', 'r') as schema_file:
            register_schema = json.load(schema_file)

        try:
            validate(instance = json_data, schema = register_schema, format_checker = FormatChecker())
            if not validate_password(json_data["password"]):
                            raise WeakPassword()
            return True
        except ValidationError as e:
            match e.validator:
                case 'required':
                    return {
                        'message': f'Missing {e.message.split("'")[1]} field'
                    }
                case 'type' | 'pattern':
                    return {
                        'message': f'Invalid {e.path[0]} field'
                    }
                case 'format':
                    return {
                        'message': 'Invalid email address'
                    }
                case 'minLength':
                    return {
                        'message': 'Password must be at least 12 characters and include uppercase, lowercase, numbers, and special characters'
                    }
        except WeakPassword:
                    return {
                        'message': 'Weak password. Password must be more than 12 characters long and include uppercase, lowercase, numbers, and special characters'
                    }

    if type_of_operation == 'Login':
        with open('schemas/auth/login.json', 'r') as schema_file:
            login_schema = json.load(schema_file)

        try:
            validate(instance = json_data, schema = login_schema, format_checker = FormatChecker())
        except ValidationError as e:
            match e.validator:
                case 'required':
                    return {
                        'message': f'Missing {e.message.split("'")[1]} field'
                    }
                case 'format':
                    return {
                        'message': 'Invalid email address'
                    }

    if type_of_operation == 'Todo':
        with open('schemas/todos.json', 'r') as schema_file:
            todo_schema = json.load(schema_file)

        try:
            validate(instance = json_data, schema = todo_schema, format_checker = FormatChecker())
        except ValidationError as e:
            match e.validator:
                case 'required':
                    return {
                        'message': f'Missing {e.message.split("'")[1]} field'
                    }
                case 'minLength':
                    return {
                        'message': 'Invalid title field'
                    }


def validate_password(password: str) -> bool:
    result = Analyzer(password)
    if result.is_highly_secure:
        return True
    else:
        return False                   