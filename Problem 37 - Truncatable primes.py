def numofdigits(n):
	z = 0
	while n > 0:
		n = n // 10
		z += 1
	return z

n = 1000000

prime = [True for i in range(n+1)] 
p = 2
prime[1] = False

while (p * p <= n): 
	if (prime[p] == True): 
		for i in range(p * 2, n+1, p): 
			prime[i] = False
	p += 1

sumx = 0

for x in range(11,1000000):
	flag = 0
	if prime[x] == False:
		flag = 1
	z = x
	while z > 0:
		z = z // 10
		if prime[z] == False:
			flag = 1
	z = x
	y = numofdigits(x)
	while z > 0:
		z = z % 10**y
		y -= 1
		if prime[z] == False:
			flag = 1
	if flag == 0:
		sumx += x

print(sumx)

# Answer: 748317