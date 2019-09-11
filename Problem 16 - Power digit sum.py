def sum_of_digits(x):
	a = 0
	while x > 0:
		a = a + x % 10
		x = x // 10
	return a

print(sum_of_digits(2**1000))

# Answer: 1366