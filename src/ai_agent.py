from agent_memory import AgentMemory

class AIAgent:
    def __init__(self):
        self.memory = AgentMemory()

    def store_memory(self, key, value):
        self.memory.store_memory(key, value)

    def retrieve_memory(self, key):
        return self.memory.retrieve_memory(key)

    def clear_memory(self):
        self.memory.clear_memory()