import os
from flask import Flask, jsonify
from extensions import db, jwt
from routes.auth import auth
from dotenv import load_dotenv
from routes.todo import todo


load_dotenv()

app = Flask(__name__)
app.json.sort_keys = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo-list.db'
app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET_KEY')

db.init_app(app)
jwt.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(todo)

@app.errorhandler(404)
def handle_404(e):
    return jsonify({'message': 'The requested URL was not found on the server'}), 404

@app.errorhandler(405)
def handle_405(e):
    return jsonify({'message': 'Method not allowed for this endpoint'}), 405

@app.errorhandler(415)
def handle_415(e):
    return jsonify({'message': 'Request body is empty'}), 415


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug = True)

