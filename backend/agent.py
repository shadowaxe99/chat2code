class Agent:
    def __init__(self):
        self.name = 'Agent1'

    def say_hello(self):
        print(f'Hello, I am {self.name}')


if __name__ == '__main__':
    agent = Agent()
    agent.say_hello()