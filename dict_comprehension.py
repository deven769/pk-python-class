result = { i:i**2 for i in range(5) }
print(result)


### map, filter, reduce
#lambda function

def total(a,b):
	return a + b
print(total(4,5))

total = lambda a,b : a + b
print(total(7,5))