number = int(input("Enter a number to check it is Prime or Not : "))
# count check the how many times numbers is divided
count = 0 
for i in range(1, number + 1):
    if number % i == 0:
        count = count + 1
if count == 2:
    # number is prime if it is divided by onlu 2 times on 1 and itself.
    print("{} is a Prime Number".format(number))
else:
    print("{} is not a Prime Number.".format(number))