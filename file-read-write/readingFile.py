import os.path

filepath = 'text.txt'
if not os.path.isfile(filepath):
    print('There is no file that name.')
else:
    with open(filepath) as file:
        # text = file.readlines()
        text = file.read().splitlines()
        num = 0
        for line in text:
            num += 1
            print(str(num) + ' ' + line)
