# Todo-List-API

## Description
Todo-List-API is a RESTful API to allow users to manage their to-do list. The system focuses on secure task management, allowing each user to organize and control their tasks.

## About the Project
This project is part of the **Backend Projects** track from [Roadmap.sh](https://roadmap.sh/projects/todo-list-api). It was developed to master key concepts such as RESTful API design, secure user authentication, and database integration. I decided to develop this API to apply the knowledge acquired in the programming modules of my first year in **Networking and Computer Systems**. As I continue my studies, I want to use what I learned in my programming classes. I want to practice and learn how to build real and secure backend services.

## Build with

* **Languages:** Python 3.12.3
* **Framework**: Flask 3.0.2
* **Database**: Flask-SQLAlchemy 3.0.3
* **Validation:** jsonschema 4.10.3

## Security

To ensure the security of the API and user data against unauthorized changes or attacks, I used the following libraries:

* **Authentication:** Flask-JWT-Extended 4.7.4
* **Password Hashing:** Flask-Bcrypt 1.0.1
* **Password Validation:** password-library 0.4.2

## Project Structure

```text
Todo-List-API/
│─── .gitignore
│─── app.py
│─── README.md
│─── requirements.txt
│─── extensions.py
│─── models.py
│─── tokens.py
│─── routes/
│    │─── auth.py
│    │─── todo.py
│─── schemas/
│    │─── auth/
│    │    │─── register.json
│    │    │─── login.json
│    │─── todos.json
│    │─── validation.py
│─── services/
│    │─── todo_services.py
│    │─── user_services.py
```

## Prerequisites

Before setting up the project, ensure you have the following installed on your system:

*   **Python:** Version 3.12.3 or higher.
*   **pip:** The Python package manager, used to install project dependencies.
*   **Git:** Necessary to clone the repository from GitHub.

## Dependencies

The project uses external libraries. To install them, execute:

```bash
pip install -r requirements.txt
```

## Configuration

To ensure security, this project uses environment variables. Create a `.env` file in the root of the project with the following content:

```env
JWT_SECRET_KEY = "your_secret_key"
```

## Cloning the Repository

To get a local copy of the project, run the following command in your terminal:

```bash
git clone "https://github.com/simao-tavares/Todo-List-API.git"

cd Todo-List-API
```

## Running the project

After installing the dependencies and configuring the `.env` file, you can start the application with the command:

```bash
python3 app.py
```
Note: Ensure you are running the command within the project's root folder.

To test the endpoints, use tools like [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/). Create a new request, select the desired method (`GET`, `POST`, `PUT`, `DELETE`), and use the base URL followed by the intended endpoint.

## API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/register` | Register a new user |
| | `/login` | Authenticate a user |
| | `/todos` | Create a new task |
| `GET` | `/todos` | List all user tasks (`?page=1&limit=10`) |
| `PUT`<br>`DELETE` | `/todos/<id>` | Update a task<br>Delete a task |


     
