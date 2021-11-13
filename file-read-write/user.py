with open('user.txt', 'r') as user:
    text = user.read().splitlines()
    username = ''
    password = ''
    while username != text[0] and password != text[1]:
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        if username == text[0] and password == text[1]:
            print('Your username and password is correct.')
        else:
            print('your username or passsword is incorrect')
