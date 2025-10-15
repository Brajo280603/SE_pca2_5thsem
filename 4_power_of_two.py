number = int(input("Enter the number :"))

if(number & (number -1) == 0):
    print(f"{number} is a power of 2")
else:
    print(f"{number} is not a power of 2")