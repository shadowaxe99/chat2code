from CommunicationManager import CommunicationManager
from LearningManager import LearningManager


class AmorphicAgent:
    def __init__(self):
        self.communication_manager = CommunicationManager()
        self.learning_manager = LearningManager()

    def interact(self, user_input):
        # Process the user input
        processed_input = self.communication_manager.process_input(user_input)

        # Use the learning manager to generate a response
        response = self.learning_manager.generate_response(processed_input)

        # Send the response to the user
        self.communication_manager.send_response(response)

    def learn(self, user_input, user_feedback):
        # Use the learning manager to learn from the user input and feedback
        self.learning_manager.learn(user_input, user_feedback)