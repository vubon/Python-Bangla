v = frozenset({1, 2, 3})
print(type(v))

print(v)

print(hash(v))

print("---------------------------")
A = frozenset({2, 3, 4, 5})
B = frozenset({1, 5, 6, 7})
print(A | B)

print(A.union(B))
