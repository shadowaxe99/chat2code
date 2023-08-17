from web3 import Web3
from solcx import compile_source


class BlockchainManager:

    def __init__(self, contract_address, private_key):
        self.web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
        self.contract_address = contract_address
        self.private_key = private_key

    def connect_to_network(self):
        print('Connecting to the blockchain network...')
        print('Connecting to the blockchain network...')

    def send_transaction(self, to_address, value):
        print('Sending a transaction...')
        print('Sending a transaction...')

    def read_data(self, contract_address):
        print('Reading data from the blockchain...')
        print('Reading data from the blockchain...')

    def manage_gas_fees(self):
        print('Managing gas fees...')
        print('Managing gas fees...')