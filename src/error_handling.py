class ErrorHandler:
    def __init__(self):
        self.errors = []

    def log_error(self, error):
        self.errors.append(error)
        print(f'Error logged: {error}')

    def get_errors(self):
        return self.errors