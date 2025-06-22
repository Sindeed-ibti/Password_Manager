import os
from cryptography.fernet import Fernet

# Generate and save a Fernet key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load the saved key
def load_key():
    with open("key.key", "rb") as file:
        return file.read()

# Ensure key.key exists and is valid (44 bytes base64)
if not os.path.exists("key.key") or os.path.getsize("key.key") != 44:
    write_key()

# Load Fernet encryption instance
key = load_key()
fer = Fernet(key)

# View stored passwords
def view():
    if not os.path.exists('passwords.txt'):
        print("No passwords saved yet.")
        return

    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            if '|' not in data:
                continue  # skip malformed lines
            try:
                user, passw = data.split("|")
                decrypted_pass = fer.decrypt(passw.encode()).decode()
                print("User:", user, "| Password:", decrypted_pass)
            except Exception as e:
                print("Error decrypting a password for user:", user)

# Add a new password
def add():
    name = input("Username: ").strip()
    pwd = input("Password: ").strip()
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + encrypted_pwd + "\n")
    print("Password saved successfully.")

# Main loop
while True:
    mode = input("Add a new password or view existing ones (view/add), or press 'q' to exit: ").lower()
    if mode == 'q':
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
