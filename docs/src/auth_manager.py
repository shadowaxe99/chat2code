class AuthManager:
    def __init__(self):
        pass

    def authenticate(self, credentials):
        username, password = credentials
        if username == 'admin' and password == 'admin':
            return True
        return False