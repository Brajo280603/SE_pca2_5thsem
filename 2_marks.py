marks = input("Enter the marks of 5 subjects separated by commas:")

marks_list = marks.split(",")

sum = 0

for i in marks_list:
    sum = sum + int(i)

avg = sum/5

if avg >= 90:
    print("Grade : A")
elif avg < 90:
    print("Grade : B")
elif avg < 80:
    print("Grade : C")
elif avg < 70:
    print("Grade : D")
elif avg < 60:
    print("Grade : F")