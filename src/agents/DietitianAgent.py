import tensorflow as tf
from Scheduler import Scheduler


class DietitianAgent:

    def __init__(self):
        self.scheduler = Scheduler()

    def provide_advice(self, user_id, user_data):
        advice = 'Eat healthy and exercise regularly.'
        return advice
        pass

    def access_scheduler(self):
        return self.scheduler