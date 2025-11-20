import hashlib
import time

# Step 1 — Create a Block class
class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    # Step 2 — Implement the hash function
    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + self.previous_hash + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    # Step 4 — Proof-of-Work
    def mine_block(self, difficulty):
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block {self.index} mined: {self.hash}")

# Step 3 — Implement the Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4 # number of leading zeros required

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        new_block = Block(len(self.chain), time.time(), data, self.get_latest_block().hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    # Step 5 — Validate the blockchain
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                print(f"Block {i} has invalid hash!")
                return False

            if current.previous_hash != previous.hash:
                print(f"Block {i} has invalid previous hash!")
                return False

            if current.hash[:self.difficulty] != '0' * self.difficulty:
                print(f"Block {i} does not meet difficulty!")
                return False

        return True

# Testing the blockchain
my_chain = Blockchain()
my_chain.add_block("First block data")
my_chain.add_block("Second block data")
my_chain.add_block("Third block data")

# Print the blockchain
for block in my_chain.chain:
    print(f"\nIndex: {block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Nonce: {block.nonce}")
    print(f"Hash: {block.hash}")

# Check if chain is valid
print("\nIs blockchain valid?", my_chain.is_chain_valid())

# Optional: tampering to see invalidation
my_chain.chain[1].data = "Hacked Data"
print("\nAfter tampering, is blockchain valid?", my_chain.is_chain_valid())