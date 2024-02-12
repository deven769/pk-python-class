class Animal:
    def speak(self):
        return "Animal speaks"

class Mammal(Animal):
    def eat(self):
        return "Mammal eats"

class Dog(Mammal):
    def bark(self):
        return "Dog barks"

# Creating instances of the classes
animal = Animal()
mammal = Mammal()
dog = Dog()

# Demonstrating multilevel inheritance
print(animal.speak())  # Output: Animal speaks
print(mammal.speak())  # Output: Animal speaks
print(mammal.eat())    # Output: Mammal eats
print(dog.speak())     # Output: Animal speaks
print(dog.eat())       # Output: Mammal eats
print(dog.bark())      # Output: Dog barks
