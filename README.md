# Mini Blockchain (Python)

This repository contains a simple, well-structured implementation of a mini blockchain system written in Python.  
It was created as part of an academic project to demonstrate the fundamental concepts behind blockchain technology.

The project covers essential blockchain mechanisms, including:

- **Block structure** (index, timestamp, data, previous hash, nonce)  
- **SHA-256 hashing**  
- **Proof-of-Work (PoW) mining**  
- **Genesis block creation**  
- **Chain validation** (detecting tampering, verifying difficulty)

The code is intentionally minimal and educational, making it easy to understand how blockchain systems work internally.

---

# How It Works

### **1. Block Class**
Each block contains:
- `index`
- `timestamp`
- `data`
- `previous_hash`
- `nonce`
- `hash`

It computes its own hash using SHA-256.

### **2. Proof of Work**
The block increments its nonce until the hash starts with a given number of zeros  
(`difficulty = 4` → hash must start with `"0000"`).

### **3. Blockchain Class**
Stores:
- The genesis block
- All mined blocks
- Validation rules to detect tampering or broken links

