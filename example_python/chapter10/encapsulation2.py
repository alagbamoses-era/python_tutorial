#!/usr/bin/python3

class Car:
    def __init__(self, make, model, year):
        # public attribute
        self.make = make

        # protected attribute (by convention, not enforced)
        self._model = model

        # private attribute (by convention, not enforced)
        self.__year = year

    # Public method to access private attribute
    def get_year(self):
        return self.__year

    # public method to set private attribute
    def set_year(self, year):
        if year > 1900: # Basic validation
            self.__year = year
        else:
            print('Invalid')
    
    # Public method
    def display_info(self):
        print(f"Car make:{self.make}, Model:{self._model}, Year:{self.get_year()}")

# Creating an instance of Car
car = Car('Toyota', 'Camry', 2020)

print(car.make) # output: Toyata


# Aceesing protected attribute (possible but not recommended)
print(car._model) # output: Camry

# Accessing private attribute (will give erroe directly)
# print(car._year)# attributeError: 'Car' object has no attribute '_year'

# Access private attribute via getter
print(car.get_year()) # output: 2020


# Acess private attribute via getter
print(car.get_year()) # output: 2020

#Modifying private attribute via setter
car.set_year(2025)

print(car.get_year()) # output: 2025

# Displaying car info
car.display_info() # output: car make:Toyaota, Model:Camry, Year:2025

