range_num = int(input("Enter the range: "))

first = 0
second = 1

fibo_series = []
fibo_series.append(first)
fibo_series.append(second)
print("Fibonacci : ")

range_num = range_num - 2

while range_num > 0:
    second = first + second
    first = second - first
    fibo_series.append(second)
    range_num = range_num-1

print(fibo_series)