data = input("Enter a string to reverse : ")
reverse= ""
for ch in data:
    reverse = ch + reverse
print("Reversed string is :", reverse)