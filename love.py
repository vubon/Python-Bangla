'''
thickness = 21#int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).ljust(thickness-1)+c+(c*i).center(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).rjust(thickness*2)+(c*thickness).ljust(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).center(thickness)+c+(c*(thickness-i-1)).center(thickness)).center(thickness*6))

'''
odd = 21
letter = 'V'

# L creation
for i in range(odd):
    print((letter*i).ljust(odd-1)+letter+(letter*i).center(odd-1))
