from app import is_valid_task_data

def test_valid_task_data():
    assert is_valid_task_data({"title": "Valid"}) is True
    assert is_valid_task_data({"title": "  "}) is False  # Whitespace
    assert is_valid_task_data({"title": 123}) is False    # Wrong type

def test_invalid_task_data():
    assert is_valid_task_data({"description": "No title"}) is False
    assert is_valid_task_data({}) is False
    assert is_valid_task_data(None) is False
