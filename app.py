from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Temporary in-memory storage
tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = {
        'id': data.get('id'),
        'text': data.get('text'),
        'completed': data.get('completed', False)
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = data.get('completed', task['completed'])
            return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404


@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    global tasks
    tasks = [t for t in tasks if t['id'] != id]
    return jsonify({'message': 'Task deleted'})

if __name__ == '__main__':
    app.run(debug=True)


