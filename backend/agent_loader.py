import importlib
import sys


class DynamicAgentLoader:
    def __init__(self):
        self.loaded_agents = {}

    def load_agent(self, agent_name):
        if agent_name in self.loaded_agents:
            return self.loaded_agents[agent_name]

        try:
            module = importlib.import_module(agent_name)
            agent_class = getattr(module, 'Agent')
            agent_instance = agent_class()
            self.loaded_agents[agent_name] = agent_instance
            return agent_instance
        except ImportError:
            print(f'Error: Could not load agent {agent_name}')
            return None

    def unload_agent(self, agent_name):
        if agent_name in self.loaded_agents:
            del sys.modules[agent_name]
            del self.loaded_agents[agent_name]
            print(f'Successfully unloaded agent {agent_name}')
        else:
            print(f'Error: Could not unload agent {agent_name}, it was not loaded')

loader = DynamicAgentLoader()
loader.load_agent('agent1')
loader.unload_agent('agent1')