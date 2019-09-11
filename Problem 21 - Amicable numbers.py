def sum_of_divisors(num):
	a = 0
	i = int(num**0.5 + 1)
	for x in range(1, i):
		if (num % x) == 0:
			a += x
			a += num / x
	a -= num
	if int(num**0.5) == num**0.5:
		a -= num**0.5
	return a

sumx = 0

for x in range(1,10000):
	y = sum_of_divisors(x)
	if (x < y) and (y < 10000):
		if x == sum_of_divisors(y):
			print(x,y)
			sumx += x + y

print(sumx)

# Answer: 31626