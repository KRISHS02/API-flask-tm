import pytest
from app import app as flask_app
import MySQLdb

@pytest.fixture(scope='module')
def app():
    # Configure test database
    flask_app.config['MYSQL_DB'] = 'test_task_db'
    flask_app.config['TESTING'] = True
    
    # Create test database
    conn = MySQLdb.connect(
        host=flask_app.config['MYSQL_HOST'],
        user=flask_app.config['MYSQL_USER'],
        password=flask_app.config['MYSQL_PASSWORD']
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS test_task_db")
    cursor.execute("USE test_task_db")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            description TEXT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

    # Establish test client
    with flask_app.test_client() as client:
        with flask_app.app_context():
            yield client

    # Teardown: Drop test database after tests
    conn = MySQLdb.connect(
        host=flask_app.config['MYSQL_HOST'],
        user=flask_app.config['MYSQL_USER'],
        password=flask_app.config['MYSQL_PASSWORD']
    )
    cursor = conn.cursor()
    cursor.execute("DROP DATABASE IF EXISTS test_task_db")
    conn.commit()
    cursor.close()
    conn.close()

@pytest.fixture
def client(app):
    return app
