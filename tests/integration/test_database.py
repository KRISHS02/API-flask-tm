import pytest
from app import create_task, get_task

def test_real_db_operations(app):
    with app.app_context():
        # Real database interaction
        task_id = create_task("Real Task", "Integration test")
        task = get_task(task_id)
        
        assert task is not None
        assert task[1] == "Real Task"
