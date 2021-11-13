num = int(input("Enter your number: "))

def prime_check(num):
    if num < 2:
        return False
    else:
        if num == 2:
            return True
        else:
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True
                

#print(prime_check(num))

if prime_check(num) is True:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number.")


