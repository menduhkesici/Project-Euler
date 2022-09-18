def isPrime(n):
	if n < 0:
		return False
	for x in range(2, int(n**0.5) + 1):
		if n % x == 0:
			return False # NOT prime number
	return True # prime number

max_primes = 0
max_a_b = 0

for a in range(-999,1000):
	for b in range(-1000,1001):
		n = 0
		while True:
			quad_exp = n**2 + a * n + b
			if isPrime(quad_exp) == True:
				n += 1
			else:
				break
		if (n - 1) > max_primes:
			max_primes = n - 1
			max_a_b = a * b

print(max_a_b)

# Answer: -59231