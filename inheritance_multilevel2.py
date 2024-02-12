class Animal:
    def __init__(self, species):
        self.species = species
        print("Animal constructor called")

class Mammal(Animal):
    def __init__(self, species, sound):
        super().__init__(species)  # Calling superclass constructor
        self.sound = sound
        print("Mammal constructor called")

class Dog(Mammal):
    def __init__(self, species, sound, breed):
        super().__init__(species, sound)  # Calling superclass constructor
        self.breed = breed
        print("Dog constructor called")

# Creating instances of Dog
dog = Dog("Canine", "Woof!", "Labrador")

# Accessing attributes
print(dog.species)  # Output: Canine
print(dog.sound)    # Output: Woof!
print(dog.breed)    # Output: Labrador
