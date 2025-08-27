import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        # Genesis block
        self.create_block(previous_hash='0')

    def create_block(self, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'previous_hash': previous_hash,
            'hash': ''
        }
        block['hash'] = self.hash(block)
        self.pending_transactions = []
        self.chain.append(block)
        return block

    def add_transaction(self, sender, receiver, amount):
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
            'timestamp': time()
        }
        self.pending_transactions.append(transaction)
        return transaction

    def hash(self, block):
        block_copy = block.copy()
        block_copy['hash'] = ''
        encoded_block = json.dumps(block_copy, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def get_chain(self):
        return self.chain

# ----------------- USAGE -----------------
blockchain = Blockchain()

# Add financial transactions
blockchain.add_transaction("Alice", "Bob", 50)
blockchain.create_block(previous_hash=blockchain.chain[-1]['hash'])

blockchain.add_transaction("Bob", "Charlie", 30)
blockchain.add_transaction("Alice", "David", 20)
blockchain.create_block(previous_hash=blockchain.chain[-1]['hash'])

# Print blockchain (transaction ledger)
for block in blockchain.get_chain():
    print(json.dumps(block, indent=4))
