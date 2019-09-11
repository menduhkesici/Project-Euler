a = 1
b = 1
total = 0

while b <= 4000000:
	if b % 2 == 0:
		total += b
	h = a + b
	a = b
	b = h

print(total)

# Answer: 4613732