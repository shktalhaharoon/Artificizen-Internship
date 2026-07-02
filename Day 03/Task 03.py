names = ["Talha", "Abdullah", "Huzaifa", "Tuaha", "Ali", "Hussain"]


def check(word):
    if len(word) > 5:
        return True
    else:
        return False
result = list(filter(check, names))
print(result)