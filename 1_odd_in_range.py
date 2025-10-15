start_range = int(input("enter the start of range:"))
end_range = int(input("enter the end of range:"))

for i in range(start_range,end_range+1):
    if (i%2 != 0):
        print(i)