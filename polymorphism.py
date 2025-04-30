class Bird:
    def intro(self):
        print("There are many types of birds.")
    
    def flight(self):
        print("Most of the birds can fly but some cannot.")

class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")

# Demonstrating polymorphism
def bird_flight(bird):
    bird.intro()
    bird.flight()

bird1 = Sparrow()
bird2 = Ostrich()

bird_flight(bird1)
bird_flight(bird2)