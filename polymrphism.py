# Experiment 6:
# Polymorphism is an OOP concept that means “one name, many forms.”
# It allows the same method or function name to perform different 
# actions depending on the object or arguments used.
# There are different ways to achieve polymorphism in Python. 
# Two easy examples are method overriding and method overloading using default arguments.

#  Q.1 polymorphism using method overriding
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()
# explanation:The Animal class has a sound() method.
# Dog and Cat override the same method and provide their own implementation.
# Thus, the same sound() method behaves differently for different objects.

#Q.2 polymorphism using method overloading
class Calculator:
    def add(self, a, b=0):
        print(a + b)

c = Calculator()

c.add(10)
c.add(10, 20)
# The same add() method can work with one or two arguments.
# When only one value is given, b automatically becomes 0.
# Thus, the same method can be used in different ways.