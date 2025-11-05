import math

def area_triag():
    sides_input = input("Enter the 3 side lengths (e.g., 3,4,5): ")
    sides_str = sides_input.split(',')

    if len(sides_str) != 3:
        print("Error: Please enter exactly three side lengths separated by commas.")
        return

    try:
        a, b, c = [float(s.strip()) for s in sides_str]
    except ValueError:
        print("Error: All inputs must be valid numbers.")
        return

    if a <= 0 or b <= 0 or c <= 0:
        print("Error: Side lengths must be positive numbers.")
        return

    if not (a + b > c and a + c > b and b + c > a):
        print(f"Error: Sides {a}, {b}, {c} do not form a valid triangle (Inequality violated).")
        return

    s = (a + b + c) / 2
    area_squared = s * (s - a) * (s - b) * (s - c)

    area = math.sqrt(max(0, area_squared))

    print(f"Semi-perimeter (s): {s:.2f}")
    print(f"Area of the triangle: {area:.2f}")
    
area_triag()
