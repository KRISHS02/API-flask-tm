import pytest
import MySQLdb
from app import app as flask_app

@pytest.fixture(scope='module')
def app():
    flask_app.config['TESTING'] = True
    flask_app.config['MYSQL_DB'] = 'test_task_db'
    
    # Setup test database
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
    
    yield flask_app
    
    # Teardown
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
    return app.test_client()
