class LearningManager:
    def __init__(self):
        # Initialize the learning manager
        self.model = None

    def train_model(self, data):
        # Train the model
        self.model = 'trained_model'
        print('Model trained')

    def evaluate_model(self, data):
        # Evaluate the model
        if self.model:
            print('Model evaluated')
            return 'model_evaluation'
        else:
            print('No model trained yet.')
            return 'No model trained yet.'