limit = 1 + 100
number = 0

for x in range(1,limit):
	for y in range(1,limit):
		if (x != y):
			number = number + x * y

print(number)

# Answer: 25164150