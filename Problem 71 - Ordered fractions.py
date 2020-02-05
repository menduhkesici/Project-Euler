max_val = 0

for d in range(1,10**6 + 1):
	for n in range(int(max_val * d), int(d * 3 / 7) + 1):
		if (n / d) < (3 / 7):
			if max_val < (n / d):
				max_val = (n / d)
				max_n = n

print(max_n)

# Answer: 428570