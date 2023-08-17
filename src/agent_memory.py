class AgentMemory:
    def __init__(self):
        # Initialize agent memory
        self.memory = {}

    def store_memory(self, key, value):
        # Store memory in agent's memory
        self.memory[key] = value

    def retrieve_memory(self, key):
        # Retrieve memory from agent's memory
        return self.memory.get(key, None)