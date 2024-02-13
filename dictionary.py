

this_dict = {"name":"Ram",
			"age":25,
			"height":7
			"more_data": {"study_info":"aslkdfj"}
			}
for key, value in this_dict.items():
	print(key,value)
	# print(this_dict[i])


this_dict.pop("age")

this_dict['name'] = 'shyam'
print(this_dict)

print(this_dict.get('name'))

