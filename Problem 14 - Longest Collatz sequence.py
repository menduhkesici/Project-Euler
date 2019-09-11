def chain(x):
	z = 1
	while x != 1:
		if x % 2 == 1:
			x = (3 * x + 1) / 2
			z = z + 2
		if x % 2 == 0:
			x = x / 2
			z = z + 1
	return z + 1

max_chain = 1

for a in range(1,1000001):
	b = chain(a)
	if b > max_chain:
		max_chain = b
		starting_number = a

print(starting_number)

# Answer: 837799