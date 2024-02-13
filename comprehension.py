numberList = [1,2,3,4,5,6]


result = [i**2 for i in  numberList if i%2==0]
print(result)


def squareNumber(numb):
	result = []
	for i in numb:
		if i % 2 == 0:
			result.append(i**2)
	return result

result = squareNumber(numberList)
print(result)
