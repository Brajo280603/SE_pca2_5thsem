sentence = input("Enter the sentence : ")

lower_count = 0
upper_count = 0

for i in list(sentence):
    if i.islower():
        lower_count = lower_count + 1
    elif i.isupper():
        upper_count = upper_count + 1
    
print(f"The number of uppercase alphabets : {upper_count}\nThe number of lowercase alphabets : {lower_count}")