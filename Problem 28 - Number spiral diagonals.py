sumx = 1
a = 1
n = 2

for x in range(2,502):
	for y in range(1,5):
		a += n
		sumx += a
	n += 2

print(sumx)

# Answer: 669171001