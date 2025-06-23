def test_api_create_task(client):
    response = client.post('/tasks', json={
        "title": "API Test",
        "description": "Test task creation"
    })
    assert response.status_code == 201
    assert 'id' in response.json

def test_api_get_tasks(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_api_update_task(client):
    # Create task
    create_res = client.post('/tasks', json={"title": "Update Test"})
    task_id = create_res.json['id']
    
    # Update task
    update_res = client.put(f'/tasks/{task_id}', json={
        "title": "Updated Title"
    })
    assert update_res.status_code == 200
    
    # Verify update
    get_res = client.get(f'/tasks/{task_id}')
    assert get_res.json['title'] == "Updated Title"

def test_api_delete_task(client):
    # Create task
    create_res = client.post('/tasks', json={"title": "Delete Test"})
    task_id = create_res.json['id']
    
    # Delete task
    delete_res = client.delete(f'/tasks/{task_id}')
    assert delete_res.status_code == 200
    
    # Verify deletion
    get_res = client.get(f'/tasks/{task_id}')
    assert get_res.status_code == 404
