z = 10  # Global variable


def sum():
    x = 10  # Local variable
    # total = x + z
    return x + z


print(sum())


def modify():
    # z = 7
    y = 5
    return y + z


print(modify())
