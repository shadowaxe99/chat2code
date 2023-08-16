from ai_agent import AIAgent

class AIFramework:
    def __init__(self):
        self.agents = []

    def add_agent(self, agent):
        if isinstance(agent, AIAgent):
            self.agents.append(agent)
        else:
            raise TypeError('agent must be an instance of AIAgent')

    def start_all_agents(self):
        for agent in self.agents:
            agent.start_interaction()

    def stop_all_agents(self):
        for agent in self.agents:
            agent.stop_interaction()