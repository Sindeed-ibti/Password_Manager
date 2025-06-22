# Password_Manager

This is a simple terminal-based password manager built with Python. It securely stores usernames and passwords in a local file using Fernet encryption from the cryptography library. The encryption key is generated once and saved in a separate key.key file.

Features:

Add new usernames and encrypted passwords

View stored credentials with automatic decryption

Secure storage using 32-byte Fernet symmetric key

Graceful handling of errors and malformed data

#Caution
For educational use only. Avoid storing sensitive credentials in plaintext files for production use.
