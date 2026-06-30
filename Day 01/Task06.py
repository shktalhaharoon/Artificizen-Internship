numbers = [10, 31, 98, 28, 12, 0]
largest = numbers[0]
smallest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
print("Largest number is : ", largest)
print("Smallest number is : ", smallest)