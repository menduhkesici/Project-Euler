cache = {}

for d in range(1, 12001):
	print(d)
	for n in range(1, d):
		if (1 / 2) > (n / d) and (n / d) > (1 / 3):
			cache[(n / d)] = True

print(len(cache))

# Answer: 7295372