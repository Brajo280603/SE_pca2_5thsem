bin = input("Enter binary number :")

gray = bin[0]

for i in range(1,len(bin)):
    gray = gray + str(int(bin[i-1])^int(bin[i]))
    
print(f"Gray code is : {gray}")
