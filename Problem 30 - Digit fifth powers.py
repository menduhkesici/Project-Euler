f = []
for x in range(0,10):
	f.append(x**5)

sumy = 0

for x in range(10,1000000):
	z = x
	sumx = 0
	while(z > 0):
		y = z % 10
		z = z // 10
		sumx += f[y]
	if sumx == x:
		sumy += x

print(sumy)

# Answer: 443839