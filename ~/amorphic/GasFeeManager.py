from web3 import Web3


class GasFeeManager:
    def __init__(self):
        # Initialize the gas fee manager
        self.web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

    def calculate_gas_fee(self, transaction):
        # Calculate the gas fee for a transaction
        gas_estimate = self.web3.eth.estimateGas(transaction)
        gas_price = self.web3.eth.gasPrice
        return gas_estimate * gas_price

    def pay_gas_fee(self, transaction, private_key):
        # Pay the gas fee for a transaction
        gas_fee = self.calculate_gas_fee(transaction)
        transaction['gas'] = gas_fee
        signed_txn = self.web3.eth.account.signTransaction(transaction, private_key)
        txn_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return txn_hash