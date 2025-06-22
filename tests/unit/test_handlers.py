from unittest.mock import patch, MagicMock
from app import app

def test_create_task_handler():
    with app.test_request_context(json={"title": "Mocked Task"}):
        # Mock database interactions
        with patch('app.mysql') as mock_mysql:
            mock_cursor = MagicMock()
            mock_mysql.connection.cursor.return_value = mock_cursor
            mock_cursor.lastrowid = 1
            
            # Call the actual handler
            from app import add_task
            response = add_task()
            
            # Verify mocks were called
            mock_cursor.execute.assert_called_once()
            assert response.status_code == 201
            assert b'Task added' in response.data

def test_update_task_handler():
    with app.test_request_context(json={"title": "Updated Task"}):
        with patch('app.mysql') as mock_mysql:
            mock_cursor = MagicMock()
            mock_mysql.connection.cursor.return_value = mock_cursor
            
            # Mock existing task
            mock_cursor.fetchone.return_value = (1, "Old Task", "Description")
            
            from app import update_task
            response = update_task(1)
            
            mock_cursor.execute.assert_called()
            assert response.status_code == 200
