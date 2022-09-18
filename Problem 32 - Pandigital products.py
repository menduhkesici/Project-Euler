# returns True if the given three numbers make up a pandigital number
def isPan(a, b, c):
	table = [0] * 10

	for i in [a, b, c]:
		while (i > 0):
			temp = i % 10
			if temp == 0:
				return False
			table[temp] += 1
			i = int(i / 10)

	for x in range(1,10):
		if (table[x] != 1):
			return False
	return True
	
total = 0
cache = {}

for x in range(1,100000):
	for y in range(x,int(10**5 / x)):
		if (isPan(x, y, (x * y)) == True):
			if ((x * y) not in cache):
				cache[(x * y)] = True
				total += x * y
				
print(total)

# Answer: 45228