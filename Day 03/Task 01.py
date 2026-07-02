def add(*numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total
print(add(10,0,30,90,35,59))