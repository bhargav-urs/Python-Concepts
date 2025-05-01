class Animal:
    # Simulated method overloading using default arguments
    def speak(self, sound=None):
        if sound:
            print(f"The animal says: {sound}")
        else:
            print("The animal makes a sound")

class Dog(Animal):
    # Method overriding: changing how 'speak' works
    def speak(self, sound=None):
        print("The dog barks")

# Create objects
a = Animal()
d = Dog()

# Method Overloading (simulated) because Python does not support method overloading
print("Animal class:")
a.speak()            # Output: The animal makes a sound
a.speak("Roar")      # Output: The animal says: Roar

# Method Overriding
print("\nDog class:")
d.speak()            # Output: The dog barks
d.speak("Woof")      # Output: The dog barks (overridden behavior)