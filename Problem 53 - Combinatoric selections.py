def comb(num1, num2):
	total = 1
	if (num2 > (num1 / 2)):
		num2 = num1 - num2
	for x in range((num1 - num2 + 1), num1 + 1):
		total *= x
	for x in range(1, num2 + 1):
		total /= x
	return int(total)

total = 0

for n in range(1, 101):
	for r in range(1,int(n / 2) + 1):
		if (comb(n, r) > 10**6):
			print(n,r)
			total += n + 1 - 2 * r
			break

print(total)

# Answer: 4075