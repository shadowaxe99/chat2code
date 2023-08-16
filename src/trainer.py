class Trainer:
    def __init__(self):
        self.training = None

    def train(self, subject):
        # Train on the given subject
        if subject == 'course':
            self.training = 'Course training in progress...'
            return self.training
        elif subject == 'tutorial':
            self.training = 'Tutorial training in progress...'
            return self.training
        elif subject == 'guide':
            self.training = 'Guide training in progress...'
            return self.training
        else:
            return 'Invalid subject'