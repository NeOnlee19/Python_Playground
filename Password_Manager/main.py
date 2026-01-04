from cryptography.fernet import Fernet

def load_key():
    f = open("key.key", "rb")
    key = f.read()
    f.close()
    return

master_pwd = input("Enter master password: ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) '''

def view():
    with open("password.txt", "r") as file:
        for line in file.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("User:", user, "Password:", password)

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as file:
        file.write(name + "|" + str(fer.encrypt(pwd.encode())) + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones? (add/view/quit): ").lower()
    if mode == "quit":
        break

    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode")
        continue