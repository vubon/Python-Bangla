'''
1+2+3+4+5 = n(n+1)/2 = 15
5(5+1)/2 = 15
'''

a = int(input("Enter your first number: "))
b = int(input("Enter your last number: "))
total = b*(b+1)// 2
print("Sum: ", total)

result = 0
for i in range(a, b+1):
    result += i
print("Sum by for loop: ", result)

    
