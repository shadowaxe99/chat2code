class Agent:
    def __init__(self):
        self.status = 'idle'

    def run(self):
        self.status = 'running'

    def stop(self):
        self.status = 'idle'

    def get_status(self):
        return self.status