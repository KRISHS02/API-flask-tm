import pytest
from app import create_task, get_task

def test_real_db_operations(app):
    with app.app_context():
        task_id = create_task("Real Task", "Integration test")
        task = get_task(task_id)
        assert task is not None
        assert task['title'] == "Real Task"  # Access by key not index
