class AgentSystem:

    def __init__(self):
        self.agents = {}

    def start(self):
        print('Starting the agent system...')

    def stop(self):
        print('Stopping the agent system...')

    def get_agent_by_id(self, agent_id):
        if agent_id in self.agents:
            return self.agents[agent_id]
        else:
            print('Agent ID not found.')
            return None