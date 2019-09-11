def sum_of_digits(x):
	a = 0
	while x > 0:
		a = a + x % 10
		x = x // 10
	return a

y = 1

for x in range(1,101):
	y *= x

print(sum_of_digits(y))

# Answer: 648