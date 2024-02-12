

class Animal:
	def __init__(self, species):
		self.species = species
	def sound(self):
		pass

class Dog:
	def sound_dog(self):
		return 'Woof'

class Cat(Dog, Animal):
	def sound(self):
		return 'Meow'

cat = Cat('cat')
print(cat.sound_dog())
