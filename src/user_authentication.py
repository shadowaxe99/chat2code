from src.AmorphicAI import AmorphicAI


class UserAuthentication:
    def __init__(self):
        pass

    def authenticate_user(self, username, password):
        ai_agent = AmorphicAI()
        ai_agent.authenticate_user(username, password)
        # Authenticate the user
        result = 'User authenticated'
        return result
