def test_update_task_handler():
    with app.test_request_context(json={"title": "Updated Task"}):
        with patch('app.mysql') as mock_mysql:
            mock_cursor = MagicMock()
            mock_mysql.connection.cursor.return_value = mock_cursor
            
            # Return a DICT to match DictCursor behavior
            mock_cursor.fetchone.return_value = {
                'id': 1, 
                'title': 'Old Task', 
                'description': 'Description'
            }
            
            from app import update_task
            result = update_task(1)
            response, status_code = result
            assert status_code == 200
