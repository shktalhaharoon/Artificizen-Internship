numbers = [1,0,2,32,14,2,5,3,2,1,2,4,5,3]


def most_frequent(numbers):
    frequent = numbers[0]
    max_count = 0
    for i in numbers:
        count = 0
        for j in numbers:
            if i == j:
                count = count + 1
        if count > max_count:
            max_count = count
            frequent = i
    return frequent


answer = most_frequent(numbers)
print("Most frequent element is:", answer)