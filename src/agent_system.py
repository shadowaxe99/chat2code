class AgentSystem:
    def __init__(self):
        self.agents = []
        self.tasks = []

    def start(self):
        # TODO: Implement the functionality to start the agent system
        pass

    def stop(self):
        # TODO: Implement the functionality to stop the agent system
        pass

    def get_all_agents(self):
        return self.agents

    def get_agent_by_id(self, id):
        for agent in self.agents:
            if agent.id == id:
                return agent
        return None

    def get_agent_tasks_by_id(self, id):
        agent_tasks = []
        for task in self.tasks:
            if task.agent_id == id:
                agent_tasks.append(task)
        return agent_tasks

    def get_all_tasks(self):
        return self.tasks

    def get_task_by_id(self, id):
        for task in self.tasks:
            if task.id == id:
                return task
        return None

    def add_agent(self, agent):
        self.agents.append(agent)

    def add_task(self, task):
        self.tasks.append(task)