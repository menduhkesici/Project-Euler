def num_of_divisors(num):
	a = 0
	i = int(num**0.5 + 1)
	for x in range(1, i):
		if (num % x) == 0:
			a += 1
	if int(num**0.5) == num**0.5:
		return 2 * a - 1
	else:
		return 2 * a

tri = 1
add = 2

while(num_of_divisors(tri) <= 500):
	tri += add
	add += 1

print(tri)

# Answer: 76576500