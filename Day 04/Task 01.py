class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def show(self):
        print("Car Brand:", self.brand)
        print("Car Model:", self.model)
        print("Car Year:", self.year)
        
car = Car("Toyota", "Corolla", 2022)

car.show()