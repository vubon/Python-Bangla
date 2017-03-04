'''
import time
filename = "file.txt"
with open(filename, 'w') as file:
    check = time.time()
    text = file.write('I am a Bangladeshi.')
    print(check)
    file.close()

'''
with open('test1.txt', 'w') as file:
    file.write('Testing')
    file.close()
