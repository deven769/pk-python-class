
class Person:
	def __init__(self, first_name,last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def getFullName(self):
		return self.first_name + ' ' + self.last_name

person1 = Person("ram","Adk", 25)
person2 = Person("shyam", 'Thapa', 30)
print(person1.getFullName())
print(person2.getFullName())
# print(person1.age)
# print(person2.age)

