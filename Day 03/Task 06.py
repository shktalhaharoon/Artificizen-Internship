# Mutable objects like lists can be modified.
#  If they are used as default arguments
# Python creates them only once and reuses the same object every time the function is called.
#  This can lead to unexpected results because changes made in one function call remain in future calls.

def add_name(name=[]):
    name.append("Talha")
    print(name)
add_name()
add_name()
add_name()



def greet(name="Talha"):
    print("Hey ", name)
greet()
greet("Haroon")