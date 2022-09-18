n = 0
d = 0
product = 1
x = 10

while x <= 1000000:
	n += 1
	d += len(str(n))
	if d >= x:
		product *= int(str(n)[x - d - 1])
		x *= 10

print(product)

# Answer: 210