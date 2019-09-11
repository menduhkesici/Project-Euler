def sum_of_divisors(num):
	a = 0
	i = int(num**0.5 + 1)
	for x in range(1, i):
		if (num % x) == 0:
			a += x
			a += num / x
	a -= num
	if int(num**0.5) == num**0.5:
		a -= num**0.5
	return a

arr = []

for x in range(1,28123):
	if sum_of_divisors(x) > x:
		arr.append(x)

l = len(arr)
sumx = 0

for z in range(0,28124):
	a = 0
	for x in range(0,l):
		if z > arr[x]:
			if (z - arr[x]) in arr:
				a = 1
				break
		else:
			break
	if a == 0:
		print(z)
		sumx += z

print(sumx)

input()

# Answer: 4179871