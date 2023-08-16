import json

class DataStorage:
    def __init__(self):
        # Initialize the data storage
        self.data = {}

    def store_data(self, key, value):
        # Store data
        self.data[key] = value
        with open('data.json', 'w') as f:
            json.dump(self.data, f)
        print(f'Data stored: {key} = {value}')

    def retrieve_data(self, key):
        # Retrieve data
        with open('data.json', 'r') as f:
            self.data = json.load(f)
        retrieved_data = self.data.get(key, None)
        if retrieved_data is not None:
            print(f'Data retrieved: {key} = {retrieved_data}')
        else:
            print(f'No data found for key: {key}')
        return retrieved_data