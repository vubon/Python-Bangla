a = {1,2,3}
b = {2,3,4,5}
print("Union set")
#Symobolic method
print(a | b)

#union() method
print(a.union(b))

print("Intersection set")
A = {1,2,3}
B = {3,4,5}
#Symbolic method
print(A & B)

#intersection() method
print(A.intersection(B))

print("Set Difference")
A = {1,2,3}
B = {3,4,5}
#Symbolic method
print(A - B)
print(B - A)
#intersection() method
print(A.difference(B))
print(B.difference(A))
	
print("Set membershipt test")
python = set("Python")
print("P" in python)
print("a" not in python)
print("a" in python)
