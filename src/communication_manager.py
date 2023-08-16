class CommunicationManager:
    def __init__(self):
        # Initialize the communication manager
        self.messages = []

    def send_message(self, message):
        # Send a message
        self.messages.append(message)
        print(f'Message sent: {message}')

    def receive_message(self):
        # Receive a message
        if self.messages:
            received_message = self.messages.pop(0)
            print(f'Message received: {received_message}')
            return received_message
        else:
            print('No messages to receive.')
            return None