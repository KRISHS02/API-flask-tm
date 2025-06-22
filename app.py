from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Krish@2002'  # REPLACE WITH YOUR PASSWORD
app.config['MYSQL_DB'] = 'task_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  # For dictionary-style results

mysql = MySQL(app)

# Auto-create database and table
with app.app_context():
    try:
        # Connect without specifying database
        conn = MySQLdb.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD']
        )
        cursor = conn.cursor()
        
        # Create database if not exists
        cursor.execute("CREATE DATABASE IF NOT EXISTS task_db")
        cursor.execute("USE task_db")
        
        # Create tasks table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(100) NOT NULL,
                description TEXT
            )
        """)
        conn.commit()
        print("✅ Database and table created successfully!")
        
    except Exception as e:
        print(f"❌ Database setup error: {str(e)}")
    finally:
        cursor.close()
        conn.close()

# API Endpoints
@app.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM tasks")
        tasks = cur.fetchall()
        cur.close()
        return jsonify(tasks)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tasks', methods=['POST'])
def add_task():
    try:
        data = request.get_json()
        if not data or 'title' not in data:
            return jsonify({'error': 'Title is required'}), 400
            
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO tasks (title, description) VALUES (%s, %s)",
            (data['title'], data.get('description', ''))
        )
        mysql.connection.commit()
        task_id = cur.lastrowid
        cur.close()
        return jsonify({'id': task_id, 'message': 'Task added'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
            
        cur = mysql.connection.cursor()
        # Check if task exists
        cur.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
        task = cur.fetchone()
        if not task:
            return jsonify({'error': 'Task not found'}), 404
            
        # Update task
        title = data.get('title', task['title'])
        description = data.get('description', task['description'])
        cur.execute(
            "UPDATE tasks SET title = %s, description = %s WHERE id = %s",
            (title, description, task_id)
        )
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'Task updated'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        cur = mysql.connection.cursor()
        # Check if task exists
        cur.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
        task = cur.fetchone()
        if not task:
            return jsonify({'error': 'Task not found'}), 404
            
        cur.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'Task deleted'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Frontend Routes
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

def is_valid_task_data(data):
    """Validate task data for unit testing"""
    return data and 'title' in data and isinstance(data.get('title'), str) and data['title'].strip()

# Add these functions to support testing
def is_valid_task_data(data):
    """Validation logic for unit tests"""
    return 'title' in data and data['title'].strip()

def create_task(title, description=""):
    """Database operation wrapper for integration tests"""
    cursor = mysql.connection.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description) VALUES (%s, %s)",
        (title, description)
    )
    mysql.connection.commit()
    return cursor.lastrowid

def get_task(task_id):
    """Database operation wrapper"""
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
    return cursor.fetchone()
