# pangram is a sentence that uses all the alphabets
sentence = input("Enter the Sentence : ")

sentence = sentence.lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"

if_pangram = False

for i in list(alphabet):
    if i in sentence:
        if_pangram = True
    else:
        if_pangram = False
        break

if if_pangram:
    print(f'"{sentence}" is a pangram.')
else:
    print(f'"{sentence}" is a not a pangram')
