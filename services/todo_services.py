from models import Todo
from extensions import db
from sqlalchemy.exc import InvalidRequestError, OperationalError


class TodoServices:

    def create_todo(self, title: str, description: str, user_id: int) -> int | None:
        try:
            add = Todo(title = title, description = description, user_id = user_id)
            db.session.add(add)
            db.session.commit()
            return add.id
        except (InvalidRequestError, OperationalError, TimeoutError):
            db.session.rollback()
            return

    def find_todo_by_id(self, id: int):
        try:
            search = db.session.query(Todo).filter(Todo.id == id).first()
            if search is None:
                return False
            else:
                return True
        except (InvalidRequestError, OperationalError, TimeoutError):
            db.session.rollback()
            return

    def get_todo_userid(self, id: int):
        try:
            search = db.session.query(Todo).filter(Todo.id == id).first()
            if search is None:
                return False
            else:
                print(search)
                return search.user_id
        except (InvalidRequestError, OperationalError, TimeoutError):
            db.session.rollback()
            return

    def update_todo(self, id: int, title: str, description: str):
        try:
            search = db.session.query(Todo).filter(Todo.id == id).first()
            search.title = title
            search.description = description
            db.session.commit()
            return search.title, search.description
        except (InvalidRequestError, OperationalError, TimeoutError):
            db.session.rollback()
            return   

    def delete_todo(self, id: int):
        try:
            search = db.session.query(Todo).filter(Todo.id == id).first()
            db.session.delete(search)
            db.session.commit()
            return True
        except (InvalidRequestError, OperationalError, TimeoutError):
            db.session.rollback()
            return

    def get_todos(self, page: int, limit: int, user_id: int):
        offset = (page - 1) * limit
        data = []
        try:
            todos = db.session.query(Todo).filter(Todo.user_id == user_id).offset(offset).limit(limit).all()
            for todo in todos:
                task_json = {
                    'id': todo.id,
                    'title': todo.title,
                    'description': todo.description
                }
                data.append(task_json)
            return {
                'data': data,
                'page': page,
                'limit': limit,
                'total': db.session.query(Todo).filter(Todo.user_id == user_id).count()
            }
        except (InvalidRequestError, OperationalError, TimeoutError):
            db.session.rollback()
            return
            



        