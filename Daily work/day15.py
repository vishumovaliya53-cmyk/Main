class Car:
    def _init_(self, brand, model):  
        self.brand = brand  # Instance variable
        self.model = model  # Instance variable

    def show_details(self):  
        print(f"Brand: {self.brand}, Model: {self.model}")

# Creating objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

car1.show_details()  # Output: Brand: Toyota, Model: Corolla
car2.show_details()  # Output: Brand: Honda, Model: Civic



class Car:
    def _init_(self, brand):
        self.brand = brand

car1 = Car("Ford")
print(car1.brand)  # Output: Ford

del car1  # Object deleted

#print(car1.brand)  # ❌ NameError: car1 is not defined


class Car:
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Tesla", "Model 3")
print(car1.brand)  # Output: Tesla
print(car1.model)  # Output: Model 3

del car1.model  # Deleting attribute

# print(car1.model)  # ❌ AttributeError: 'Car' object has no attribute 'model'


class Test:
    def delete_self(self):
        del self  # ❌ This does not work

t = Test()
t.delete_self()  # No effect on the object