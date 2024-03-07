
## How It Works

### Block Class

The `Block` class represents individual blocks in the blockchain. Each block contains the following attributes:

- `index`: The index of the block in the chain.
- `timestamp`: The timestamp of when the block was created.
- `data`: The data stored in the block.
- `previous_hash`: The hash of the previous block in the chain.
- `hash`: The hash of the current block.

### Blockchain Class

The `Blockchain` class manages the blockchain and its operations. It includes the following methods:

- `create_genesis_block()`: Creates the genesis block (the first block) of the blockchain.
- `add_block(data)`: Adds a new block to the blockchain with the provided data.

## Example

Here's how you can create a simple blockchain and add blocks to it:

```python
from blockchain import Blockchain

# Create a blockchain instance
my_blockchain = Blockchain()

# Add blocks to the blockchain
my_blockchain.add_block("First Block")
my_blockchain.add_block("Second Block")
