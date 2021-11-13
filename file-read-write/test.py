z = 10
def test(x):
    global z
    z = 5 # We can modify the Global variable any time. 
    return x + z 
print(test(10))

print("---------------------------")

def local(a, b):
    sum = a + b
    return sum
print(local(10,44))
