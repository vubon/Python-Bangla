with open('user.txt', 'r') as file:
    text = file.read().splitlines()
    username = ""
    password = ""
    while username != text[0] and password != text[1]:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == text[0] and password == text[1]:
            print(" Login success")
        else:
            print("username/password is incorrect")
