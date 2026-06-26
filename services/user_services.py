from sqlalchemy.exc import InvalidRequestError, OperationalError
from extensions import db, bcrypt
from models import User


class UserServices:
    def find_user_by_email(self, email: str) -> bool | None:
        try:
            search = db.session.query(User).filter(User.email == email).first()
            if search is None:
                return False
            else:
                return True
        except (InvalidRequestError, OperationalError, TimeoutError):
            db.session.rollback()
            return

    def add_user(self, name: str, email: str, password: str) -> int | None:
        try:
            user = User(name = name, email = email, password = password)
            db.session.add(user)
            db.session.commit()
            return user.id
        except (InvalidRequestError, OperationalError, TimeoutError):
            db.session.rollback()
            return            

    def password_to_hash(self, password: str) -> str:
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        return hashed_password
        
