num = int(input("Enter your number: "))

def even_odd(num):
    if num < 1:
        return "The number is not even or odd"
    else:
        if num % 2 == 0:
            return True
        else:
            return False
        
#print(even_odd(num))
if even_odd(num) is True:
    print(num, "is an even number")
else:
    print(num, "is an odd number")
