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



        