import math

sides = input("Enter the side lengths separated by commas : ")

sides = sides.split(",")

if(len(sides) > 3):
    print("more than 3 sides entered")
    
# using heron's formula to compute area of triangle
semi_perim = 0
for i in range(0,len(sides)):
    sides[i] = float(sides[i])
    
    semi_perim = semi_perim + sides[i]


semi_perim = semi_perim / 2

area = 1

for i in range(0,len(sides)):
    temp = semi_perim - sides[i]
    area = area * temp
    
area = area * semi_perim

area = math.sqrt(area)

print(f"The area of the triangle is : {area}")