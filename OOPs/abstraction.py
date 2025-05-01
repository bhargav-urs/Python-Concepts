from abc import ABC, abstractmethod
# Abstract Base Class (ABC) module in Python -> define an abstract class and its subclasses.

# Abstract Base Class (ABC) example
class Animal(ABC):
    @abstractmethod
    # Define an abstract method
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Example usage
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.make_sound())