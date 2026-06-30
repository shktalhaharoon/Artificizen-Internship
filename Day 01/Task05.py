data = input("Enter a string: ")
reverse = ""
for ch in data:
    reverse = ch + reverse
if data == reverse:
    print("String is Palindrome.")
else:
    print("String is Not Palindrome.")