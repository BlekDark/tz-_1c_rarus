from flask import Flask, request, jsonify
from task_manager import TaskManager

app = Flask(__name__)
task_manager = TaskManager()

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    priority = data.get('priority')
    if not title or not priority:
        return jsonify({'error': 'Missing title or priority'}), 400
    task = task_manager.add_task(title, priority)
    return jsonify(task), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = task_manager.get_tasks()
    return jsonify(tasks), 200

@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    title = data.get('title')
    priority = data.get('priority')
    task = task_manager.update_task(task_id, title, priority)
    if task:
        return jsonify(task), 200
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = task_manager.delete_task(task_id)
    if task:
        return jsonify({'message': 'Task deleted'}), 200
    return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)