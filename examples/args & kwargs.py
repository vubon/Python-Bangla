def python(a, b):
    v = a + b
    print("Normal way args: ", v)


python(2, 3)


def python2(*args):
    s = args * 2
    v = a * 2
    print('duable tuple making: ',s)
    print(v)


a = (1, 2, 3, 4)
python2(a)


def python3(**kwargs):
    print('Keyword arguments: ', kwargs)


d = {'Country': 'Bangladesh', 'Capital': 'Dhaka'}
python3(Name='Vubon', Home='Dinajpur')
python3(**d)
