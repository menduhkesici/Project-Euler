def dectobin(n):
	x = 0
	a = 0
	while n > 0:
		if n % 2 == 1:
			x += 10**a
		n = n // 2
		a += 1
	return x

def numofdigits(n):
	z = 0
	while n > 0:
		n = n // 10
		z += 1
	return z

def ispalindromic(n):
	z = n
	a = numofdigits(n) - 1
	inv = 0
	while z > 0:
		inv += (z % 10) * 10**a
		z = z // 10
		a -= 1
	return inv == n

sumx = 0

for x in range(1,1000000):
	if ispalindromic(x):
		if ispalindromic(dectobin(x)):
			sumx += x

print(sumx)

# Answer: 872187