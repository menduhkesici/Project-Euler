def IsPrime(a):
	flag = 0
	for x in range(2,int(a**0.5)+1):
		if a % x == 0:
			flag = 1
			break
	if flag == 1:
		return 0
	if flag == 0:
		return 1

total = 2 + 3

# except 2 and 3, all prime numbers are 6k-1 or 6k+1

for x in range(5,2000001,6):
	if IsPrime(x) == 1:
		total = total + x

for y in range(7,2000001,6):
	if IsPrime(y) == 1:
		total = total + y

print(total)

# Answer: 142913828922