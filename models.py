from extensions import db


class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)

    def __repr__(self) -> str:
        return f'User (Id: {self.id} | Name: {self.name} | Email: {self.email} | Password: {self.password})'


class Todo(db.Model):
    __tablename__ = 'Todo'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)
    user_id = db.Column(db.ForeignKey('User.id'))

    def __repr__(self) -> str:
        return f'Todo (Id: {self.id} | Title: {self.title} | Description: {self.description} | User_id: {self.user_id})'