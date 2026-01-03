master_pwd = input("Enter master password: ")
def view():
    pass

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as file:
        file.write(name + "|" + pwd)

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