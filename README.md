# Flask Task Manager API

A simple Task Manager web API built with Flask and MySQL. This project demonstrates RESTful API design, database integration, and automated testing.

---

## Features

- **Custom REST API**: Create, read, update, and delete tasks.
- **MySQL Database**: Persistent storage for all tasks.
- **Automated Testing**: Unit, integration, and API tests with coverage.
- **Professional Structure**: Organized for clarity and maintainability.

---

## API Endpoints

| Method | Endpoint           | Description          |
|--------|--------------------|---------------------|
| GET    | `/tasks`           | List all tasks      |
| GET    | `/tasks/<id>`      | Get a single task   |
| POST   | `/tasks`           | Add a new task      |
| PUT    | `/tasks/<id>`      | Update a task       |
| DELETE | `/tasks/<id>`      | Delete a task       |

#### Example POST Body

{
"title": "Sample Task",
"description": "This is a sample."
}

text

---

## Manual API Testing

- **GET** `/tasks` — Returns all tasks
- **GET** `/tasks/<id>` — Returns a single task
- **POST** `/tasks` — Adds a new task
- **PUT** `/tasks/<id>` — Updates a task
- **DELETE** `/tasks/<id>` — Deletes a task

Tested with [Postman](https://www.postman.com/) and `curl`.

---

## Setup & Installation

1. **Clone the repository:**
git clone https://github.com/KRISHS02/flask-task-manager.git
cd flask-task-manager

text

2. **Install dependencies:**
pip install -r requirements.txt

text

3. **Configure MySQL:**
- Ensure MySQL is running.
- Update `app.py` with your MySQL credentials.

4. **Run the application:**
python app.py

text
- Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## Project Structure

flask-task-manager/
├── app.py
├── requirements.txt
├── tests/
│ ├── conftest.py
│ ├── unit/
│ │ ├── test_handlers.py
│ │ └── test_validators.py
│ ├── integration/
│ │ └── test_database.py
│ └── api/
│ └── test_api_endpoints.py
├── templates/
│ └── index.html
└── README.md

text

---

## Testing

### Test Types
- **Unit Tests**: Mocked and non-mocked logic.
- **Integration Tests**: Real database CRUD.
- **API Tests**: Endpoint functionality.

### Running Tests
pytest --cov=app --cov-report=html

text

### Coverage Report
Include a screenshot like below after running tests:

![Test Coverage](coverage_screenshot.png Stack)

- Python 3.x
- Flask
- MySQL
- pytest, pytest-cov, pytest-flask

---

## Author

- [Krish Singhal](https://github.com/KRISHS02)

---

## License

This project is for educational and demonstration purposes.
