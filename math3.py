import math 

sides=int(input("Number of sides: "))
length=int(input("Length of sides: "))



area = (sides * length**2) / (4 * math.tan(math.pi/sides))


print(int(area))