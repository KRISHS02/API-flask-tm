from app import is_valid_task_data

def test_valid_task_data():
    assert is_valid_task_data({"title": "Valid"}) is True

def test_invalid_task_data():
    assert is_valid_task_data({"description": "No title"}) is False
