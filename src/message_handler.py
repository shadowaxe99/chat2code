class MessageHandler:
    def __init__(self):
        pass

    def handle_message(self, message):
        print(f'Received: {message}')
        response = 'Message received'
        return response