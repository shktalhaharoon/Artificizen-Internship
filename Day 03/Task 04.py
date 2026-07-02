number = int(input("Enter a number to calculate the fictorial : "))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


ans = factorial(number)

print("Factorial =", ans)