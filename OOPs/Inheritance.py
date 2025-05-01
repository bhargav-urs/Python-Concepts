# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Derived class
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

# Derived class
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."

# Example usage
if __name__ == "__main__":
    animal = Animal("Generic Animal")
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    
    print(animal.speak())
    print(dog.speak())  
    print(cat.speak())  