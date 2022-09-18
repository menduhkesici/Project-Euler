a_products = 1
b_products = 1

for a in range(10,100):
	for b in range(a+1,100):
		c = a / b
		a_1 = a // 10
		a_2 = a % 10
		b_1 = b // 10
		b_2 = b % 10
		if (a_2 != 0) and (b_2 != 0):
			if (a_1 * a_2 / (b_1 * b_2) == c):
				if (a_1 == b_2) or (a_2 == b_1):
					a_products *= a
					b_products *= b

print(b_products / a_products)

# Answer: 100