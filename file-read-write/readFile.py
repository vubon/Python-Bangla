import os.path
filepath = 'test.txt'
if not os.path.isfile(filepath):
    print('There is no file that name.')
else:
    with open(filepath) as file:
        #content = file.readlines()
        content = file.read().splitlines()
        num = 0
        for line in content:
            num += 1
            print(str(num)+ ' '+ line)
            
