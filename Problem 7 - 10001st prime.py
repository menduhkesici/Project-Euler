last_prime = 3
i = 2

while i != 10001:
	last_prime = last_prime + 2
	flag = 0
	for x in range(2,int(last_prime**0.5+1)):
		if (last_prime % x == 0):
			flag = 1
			break
	if flag == 0:
		i = i + 1

print(last_prime)

# Answer: 104743