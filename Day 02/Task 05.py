sentence = input("Enter Data : ")
vowels = 0
consonants = 0
for ch in sentence:
    if ch != " ":
        if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u" or ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U":
            vowels = vowels + 1
        else:
            consonants = consonants + 1
print("Vowels =", vowels)
print("Consonants =", consonants)