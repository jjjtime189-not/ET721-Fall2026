"""
Lab 5, review of class, object, methods, and attributes
Joseph Ali-Shaw
September 16,2026
"""
print("------Example 1: class Circle------")

class Circle():
    def __init__(self,radius,color):
        self.r = radius
        self.c = color
    pi = 3.14157
    def circumference(self):
        return 2*self.pi*self.r
c1=Circle(2,'red')
print(c1.r)
print(c1.circumference())

print("------Example 2: class Rectangle------")
class Rectangle():
    def __init__(self,height,width,color):
        self.h = height
        self.w = width
        self.c = color
    pi = 3.14157
    def area(self):
        return self.w*self.h
    def perimeter(self):
            return 2*self.w+2*self.h
    """
    def drawRectangle(self):
         import matplotlib.pyplot as plt
         plt.gca().add_patch(plt.Rectangle((0,0),self.w,self.h,fc=self.c))
         plt.axis('scaled')
         plt.show()
    """
r1=Rectangle(2,3,'olive')
print(f'The perimeter of the rectange with height = {r1.h} and width = {r1.w} is {r1.perimeter()}')

"""
Car dealership's inventory management system
You are working on a python program to simulate a car dealership's inventory management 
system. The system aims to model cars and their attributes accurately.
Task 1: create a class to represent each vehicle. Each car should have attributes for 
maximum speed and mileage.
Task 2: update the class with the default color for all vehicle, "white"
Task 3: create a class method to assign seating capacity to a vehicle
Task 4: create a class method to display all the properties of an object 
class --> "The __(color) car has __ seats, with __ miles, and a maximum speed of __"
Task 5: create two instance objects of the car. One car will have a max speed of 200kph 
and mileage of 50000 kmpl with five seating capacity. The other car will have a max speed 
of 180kph mileage of 75000kmpl, four seating
"""
print("------------EXERCISE-------------------")
class cars():
    def __init__(self,maxSpeed,mileage):
        self.ms = maxSpeed
        self.m = mileage
    color = 'white'
    def capacity(self,seats):
        self.s = seats
    def display(self):
         print(f"The {self.color} car has {self.s} seats, with {self.m} miles, and a maximum speed of {self.ms} kph")
car1=cars(200,50000)
car1.capacity(5)
car2=cars(180,75000)
car2.capacity(4)
car1.display()
car2.display()