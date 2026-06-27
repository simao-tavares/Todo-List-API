from models import Todo
from extensions import db
from sqlalchemy.exc import InvalidRequestError, OperationalError


class TodoServices:

    def create_todo(self, title: str, user_id: int,  description: str = '') -> int | None:
        try:
            add = Todo(title = title, description = description, user_id = user_id)
            db.session.add(add)
            db.session.commit()
            return add.id
        except (InvalidRequestError, OperationalError, TimeoutError):
            db.session.rollback()
            return



        