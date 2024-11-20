'''
PART 1
'''
# Base Class
class Vehicle :
    def __init__(self, model, year) :
        self.model = model
        self.year = year

    def start(self):
        print("Start driving.")

    def stop(self):
        print("Stop driving.")

    def fuel_up(self):
        print("Fuel up.")

# Derived Classes
class Car(Vehicle):
    def __init__(self, model, year, num_doors) :
        super().__init__(model, year)
        self.num_doors = num_doors
    
    def __str__(self):
        return f"I am a car, model {self.model} year {self.year} and I have {self.num_doors} doors."

    def honk_horn(self) :
        print("Honk, honk!")

class Bicycle(Vehicle):
    def __init__(self, model, year, num_gears) :
        super().__init__(model, year)
        self.num_gears = num_gears

    def __str__(self):
        return f"I am a bicycle, model {self.model} year {self.year} and I have {self.num_gears} gears."

    def start(self):
        print("Start cycling.")
    
    def stop(self):
        print("Stop cycling.")
        
    def fuel_up(self):
        print("Pump the wheels and grease the chain.")
    
    def ring_bell(self) :
        print("Gling, gling!")

class Motorcycle(Vehicle):
    def __init__(self, model, year, engine_size) :
        super().__init__(model, year)
        self.engine_size = engine_size

    def __str__(self):
        return f"I am a motorcycle, model {self.model} year {self.year} and my engine is {self.engine_size} cc."

    def drive_motorway(self) :
        if (self.engine_size <= 125): 
            print("Engine too small ! Cannot drive on a motorway !")
        else:
            print("Go ahead and get on the motorway !")

car = Car("Revell", 1965, 2)
print(car)
car.start()
car.stop()
car.fuel_up()
car.honk_horn()

bicycle = Bicycle("Mk1 Burner", 1982, 5)
print(bicycle)
bicycle.start()
bicycle.stop()
bicycle.fuel_up()
bicycle.ring_bell()

motorbike = Motorcycle("Gixxer 150", 2014, 155)
print(motorbike)
motorbike.start()
motorbike.stop()
motorbike.fuel_up()
motorbike.drive_motorway()

'''
Part 2
'''
import math

# Base Class
class Shape:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"I am a {self.name}."

    def area(self):
        return print("Area not implemented in Shape.")

    def perimeter(self):
        return print("Perimeter not implemented in Shape.")
    
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return print("The area of this circle is: ", "{:.2f}".format(math.pi*self.radius**2))
    
    def perimeter(self):
        return print("The perimeter of this circle is: ", "{:.2f}".format(2*math.pi*self.radius))


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return print("The area of this rectangle is: ", "{:.2f}".format(self.length*self.width))

    def perimeter(self):
        return print("The perimeter of this rectangle is: ", "{:.2f}".format(2*self.length + 2*self.width))

shape = Shape("Triangle")
print(shape)
shape.area()
shape.perimeter()

circle = Circle("Circle",2)
print(circle)
circle.area()
circle.perimeter()

rectangle = Rectangle("Rectangle", 2,3)
print(rectangle)
rectangle.area()
rectangle.perimeter()