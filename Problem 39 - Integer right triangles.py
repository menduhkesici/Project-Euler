max_num_of_sol = 0
max_p = 0

for p in range(1,1001):
	num_of_sol = 0
	for a in range(1,int(p/2)):
		for b in range(a,int(p/2)):
			c = (a**2 + b**2)**0.5
			if (a + b + c) > p:
				break
			if (c == p - a - b):
				num_of_sol += 1
	if num_of_sol > max_num_of_sol:
		max_num_of_sol = num_of_sol
		max_p = p

print(max_p)

# Answer: 840