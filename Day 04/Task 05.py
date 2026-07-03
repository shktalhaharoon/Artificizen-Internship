class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def year (cls, name, year):
        #cls is used for current class as we use self foe current object
        age = 2026 - year
        return cls(name, age)


person = Person.year("Ali", 2005)
print(person.name)
print(person.age)