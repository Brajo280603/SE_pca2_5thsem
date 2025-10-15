number = input("Enter the number : ")

number_arr = list(number)

length = len(number_arr)

armsum = 0

for num in number_arr:
    armsum = armsum + ((int(num))**length)

if armsum == int(number):
    print(f"{number} is a Armstrong number.")
else:
    print(f"{number} is not a Armstrong number.")
