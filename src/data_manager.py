from database_manager import DatabaseManager


class DataManager:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def get_data(self, query):
        return self.db_manager.fetch_query(query)

    def update_data(self, query):
        self.db_manager.execute_query(query)