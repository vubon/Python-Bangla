a = {1, 2, 3}
b = {"Python", 2.0, (1, 2, 3)}
print("a: ", a)
print("b : ", b)
print("........................")
a = set({1, 2, 1, 2, 3})
print(a)

print("add element in set by using add() method.")
a.add(4)
print(a)

print("More items add in our set by using update() method")
a.update({5, 6})
print(a)

print("Remove item from out set by using remove() method.")
a.remove(1)
print(a)

print("Remove item from our set by using discard() method. ")
a.discard(2)
print(a)

print("clear() method ")
a.clear()
print(a)
