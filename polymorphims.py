class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    return animal.speak()

# Creating instances of different classes
dog = Dog()
cat = Cat()

# Calling the same method on different objects
print(make_animal_speak(dog))  # Output: Woof!
print(make_animal_speak(cat))  # Output: Meow!




##encapulation


class Math:
    def __init__(self, b, c):
        self.__a = b
        self._c = c 


    def getA(self):
        return self.__a

ob1 = Math(4, 3)
print(obj1.getA())
print(ob1._a)

