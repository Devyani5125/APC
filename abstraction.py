# Experiment no 6:
# Abstraction is an OOP concept that means hiding unnecessary implementation details and 
# showing only the essential features to the user.
# For example, when you use an ATM, you only see options like Withdraw, Deposit, and
#  Check Balance. You don't see the internal code that processes the transaction.
# abstract class:An abstract class is a class that is used as a base/parent class and
#  contains one or more abstract methods.
# In Python, we use the ABC module to create an abstract class
# An abstract method is a method that is declared in the parent class but 
# does not contain its actual implementation


# Q1. Abstract class with Animal
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()

from abc import ABC, abstractmethod
# explanation:from abc import ABC, abstractmethod → Imports the tools required for abstraction.
# class Animal(ABC): → Creates an abstract class named Animal.
# @abstractmethod → Makes sound() an abstract method.
# def sound(self): → Declares the method.
# pass → No implementation is given in the parent class.
# class Dog(Animal): → Dog inherits from Animal.
# def sound(self): → Dog provides the implementation of the abstract method.
# print("Dog barks") → Displays the dog's sound.
# d = Dog() → Creates a Dog object.
# d.sound() → Calls the sound() method


# Q2.Create abstract class for shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def area(self):
        print("Area of square = 25")

s = Square()
s.area()

from abc import ABC, abstractmethod
# explanation:from abc import ABC, abstractmethod → Imports abstraction tools.
# class Shape(ABC): → Creates an abstract class named Shape.
# @abstractmethod → Makes area() an abstract method.
# def area(self): → Declares the area() method.
# pass → No implementation is given in Shape.
# class Square(Shape): → Square inherits from Shape.
# def area(self): → Square implements the abstract method.
# print("Area of square = 25") → Displays the area.
# s = Square() → Creates a Square object.
# s.area() → Calls the area() method

