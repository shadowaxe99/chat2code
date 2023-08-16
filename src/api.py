from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/agents', methods=['GET'])
def get_agents():
    # Fetch all agents from the agent system
    agents = agent_system.get_all_agents()
    return jsonify(agents), 200

@app.route('/api/agents/<id>', methods=['GET'])
def get_agent(id):
    # Fetch the agent with the given ID from the agent system
    agent = agent_system.get_agent_by_id(id)
    if agent is None:
        return jsonify({'message': 'Agent not found'}), 404
    return jsonify(agent), 200

@app.route('/api/agents/<id>/tasks', methods=['GET'])
def get_agent_tasks(id):
    # Fetch the tasks of the agent with the given ID from the agent system
    tasks = agent_system.get_agent_tasks_by_id(id)
    if tasks is None:
        return jsonify({'message': 'Tasks not found'}), 404
    return jsonify(tasks), 200

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    # Fetch all tasks from the agent system
    tasks = agent_system.get_all_tasks()
    return jsonify(tasks), 200

@app.route('/api/tasks/<id>', methods=['GET'])
def get_task(id):
    # Fetch the task with the given ID from the agent system
    task = agent_system.get_task_by_id(id)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404
    return jsonify(task), 200

if __name__ == '__main__':
    app.run(debug=True)