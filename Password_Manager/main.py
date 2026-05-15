
def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            print(line.rstrip())
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(f"Name: {name}, Password: {pwd}\n")
master_pwd = input("What is the master password? ")
if master_pwd == "password123":
    mode = input("What mode do you want to use? (view/add/quit)")
    if mode == "quit":
        quit()
    if mode == "view":
        try:
            view()
        except Exception as e:
            print("No password stored yet!")
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
else:
    print("Nice try Buddy!")