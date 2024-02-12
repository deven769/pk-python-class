# Exception

def exception_handeling():
	a = input("Enter a number:")
	b = input("Enter a number:")
	try:
		result = a/b
		return result
	except ZeroDivisionError:
		# print('error ')
		# print('error ayo')
		return 'Error ayo'
	# else:
	# 	print('i am else state')
	# finally:
	# 	print('finally')

result = exception_handeling()
print(result)