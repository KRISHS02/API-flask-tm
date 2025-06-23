from unittest.mock import patch, MagicMock
from app import app

def test_create_task_handler():
    with app.test_request_context(json={"title": "Mocked Task"}):
        with patch('app.mysql') as mock_mysql:
            mock_cursor = MagicMock()
            mock_mysql.connection.cursor.return_value = mock_cursor
            mock_cursor.lastrowid = 1
            
            from app import add_task
            result = add_task()
            response, status_code = result
            assert status_code == 201

def test_update_task_handler():
    with app.test_request_context(json={"title": "Updated Task"}):
        with patch('app.mysql') as mock_mysql:
            mock_cursor = MagicMock()
            mock_mysql.connection.cursor.return_value = mock_cursor
            mock_cursor.fetchone.return_value = {
                'id': 1, 
                'title': 'Old Task', 
                'description': 'Description'
            }
            
            from app import update_task
            result = update_task(1)
            response, status_code = result
            assert status_code == 200
