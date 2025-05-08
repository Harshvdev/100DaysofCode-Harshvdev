class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self):
        return self.length*self.breadth
    
    def perimeter(self):
        return 2*(self.length+self.breadth)
    
    def __str__(self): # So it is just used to show a readable message when using print(object)
        return f"Rectangle: {self.length} x {self.breadth}"
    
class Laptop:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.__serial_number = "ABCXYZ123" # Using __ makes the attribute private that can only be acceessible withina the class.

    def get_serial_number(self, password):
         if password == "Harsh":
             return self.__serial_number
         else:
             return "Access Denied."
         
class Movie:
    def __init__(self, review_list=None):
        if review_list:
            self.review_list = review_list
        else:
            self.review_list = []

    def add_review(self, review):
        self.review_list.append(review)

    def avg_review(self):
        if not self.review_list:
            return "No reviews yet."
        return sum(self.review_list)/len(self.review_list)
    
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        return "Engine has started."

class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type, mileage):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type
        self.mileage = mileage

    def start_engine(self):
        if self.fuel_type == "Petrol":
            return "Car will start in 0.85 seconds"
        elif self.fuel_type == "Diesel":
            return "Car will start in 1 seconds."
        elif self.fuel_type == "Electricity":
            return "Car will start in 0.2 seconds."