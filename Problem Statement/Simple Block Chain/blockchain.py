import hashlib
import datetime as date


# Define the Block class
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()
    
# Define the Blockchain class    

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, date.datetime.now(), "Genesis Block", "0")

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), date.datetime.now(), data, previous_block.hash)
        self.chain.append(new_block)

chain = Blockchain()

# Add some blocks
chain.add_block("First Block")
chain.add_block("Second Block")
chain.add_block("Third Block")
chain.add_block("Fourth Block")
chain.add_block("Fifth Block")


#Print Method
def print_blockchain(blockchain):
    for block in blockchain.chain:
        print("----------",block.index,"------------")
        print("Block Index:", block.index)
        print("Timestamp:", block.timestamp)
        print("Data:", block.data)
        print("Previous Hash:", block.previous_hash)
        print("Hash:", block.hash)
        print("\n")

print_blockchain(chain)