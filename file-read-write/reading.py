filelocation = "test.txt"
with open(filelocation) as me:
    content = me.readlines()
for line in content:
    print(line)
