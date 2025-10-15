N = int(input("Enter the value of N : "))

sum = 0

for i in range(1, N + 1):
    sum = sum + (1 / i)

print(f"Answer is : {sum}")
