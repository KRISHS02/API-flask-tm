def test_api_create_task(client):
    response = client.post('/tasks', json={
        "title": "API Test",
        "description": "Test task creation"
    })
    assert response.status_code == 201
    assert 'id' in response.json

def test_api_update_task(client):
    # Create then update
    create_res = client.post('/tasks', json={"title": "Update Test"})
    task_id = create_res.json['id']
    
    update_res = client.put(f'/tasks/{task_id}', json={
        "title": "Updated Title"
    })
    assert update_res.status_code == 200
