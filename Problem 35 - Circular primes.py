n = 1000000

prime = [True for i in range(n+1)] 
p = 2
prime[0] = False
prime[1] = False

while (p * p <= n): 
	if (prime[p] == True): 
		for i in range(p * 2, n+1, p): 
			prime[i] = False
	p += 1

# 2, 3, 5, 7
sumx = 4

for x in range(11,1000001):
	z = x
	num = 0
	while z > 0:
		z = z // 10
		num += 1
	flag = 0
	z = x
	for y in range(1,num+1):
		if prime[z] == False:
			flag = 1
		z = (z % 10) * 10**(num-1) + (z // 10)
	if flag == 0:
		sumx += 1

print(sumx)

# Answer: 55