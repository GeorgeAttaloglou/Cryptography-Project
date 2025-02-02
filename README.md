# Cryptography Project

## Introduction
This is a cryptography project developed as part of a cybersecurity class assignment. It focuses on encrypting user credentials using cryptographic techniques.

## Purpose
The objective of this project is to provide hands-on experience with cryptography concepts, including hashing, encryption, and digital signatures.

## Features
This project consists of a single file, `main.py`, which allows users to:

- Enter a username and password.
- Hash the password using MD5 with a randomly generated salt.
- Encrypt the credentials using AES encryption.
- Sign the encrypted data using ECC (Elliptic Curve Cryptography).
- Store the encrypted credentials and signature in a file (`user.txt`).

## Requirements
To run this project, you need Python and the required dependencies installed.

### Dependencies
Install the required Python package before running the script:
```bash
pip install pycryptodome
```

## Execution
To execute the script, run:
```bash
python main.py
```

## How It Works
1. The user is prompted to enter a username and password.
2. The password is hashed using MD5 with a salt.
3. The hashed credentials are encrypted using AES in OFB mode.
4. The encrypted data is signed using ECC with SHA-256 hashing.
5. The encrypted data and signature are stored in `user.txt`.

## Security Considerations
- **MD5 is not secure**: While this project uses MD5 for hashing, it is not recommended for real-world applications due to vulnerabilities. A more secure alternative would be SHA-256.
- **No key persistence**: The AES key and ECC key pair are generated each time the script runs, meaning previously encrypted data cannot be decrypted in subsequent runs.
- **No decryption process**: This project demonstrates encryption and signing but does not include a mechanism for decryption and verification.

## Future Improvements
- Replace MD5 with a stronger hashing algorithm like SHA-256.
- Implement a proper key management system to allow decryption.
- Add user authentication features instead of just encrypting credentials.

## Author
This project was created for a cybersecurity course.