def num_of_dig(num):
	temp = 0
	while (num > 0):
		num = int(num / 10)
		temp += 1
	return temp

temp = 0
for x in range(0,100):
	for num in range(0,10):
		if (num_of_dig(num**x) == x):
			temp += 1
		elif (num_of_dig(num**x) > x):
			break

print(temp)

# Answer: 49