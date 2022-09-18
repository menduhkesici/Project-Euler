cache = {}

for a in range(2,101):
	for b in range(2,101):
		if a**b not in cache:
			cache[a**b] = True

print(len(cache))

# Answer: 9183