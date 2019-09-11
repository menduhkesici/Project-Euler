def factorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * factorial(n-1)

listx = list(range(0,10))

x = 1000000 - 1
sumx = 0

for y in range(9,-1,-1):
	z = (x % factorial(y+1)) // factorial(y)
	sumx += listx[z] * 10**y
	del listx[z]

print(sumx)

# Answer: 2783915460