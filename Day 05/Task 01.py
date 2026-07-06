# Parent class
class Animal:

    # This method gives a general sound for an animal
    def speak(self):
        print("Animals make Sound")

# Dog class inherits from Animal
class Dog(Animal):

    # This method overrides the speak() method of Animal
    # Now, when a Dog object calls speak(), this method will run instead
    def speak(self):
        print("Dog Barks")

# Cat class inherits from Animal
class Cat(Animal):

    # This method also overrides the speak() method of Animal
    def speak(self):
        print("Cat Meow")

# Creating objects
dog = Dog()
cat = Cat()
animal = Animal()

# Calling the speak() method
animal.speak()   # Calls the parent class method
dog.speak()      # Calls the overridden method in Dog
cat.speak()      # Calls the overridden method in Cat