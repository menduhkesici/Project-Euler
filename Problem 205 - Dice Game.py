arr4 = [0] * (9 * 4 + 1)
arr6 = [0] * (6 * 6 + 1)

for num1 in range(1, 5):
	for num2 in range(1, 5):
		for num3 in range(1, 5):
			for num4 in range(1, 5):
				for num5 in range(1, 5):
					for num6 in range(1, 5):
						for num7 in range(1, 5):
							for num8 in range(1, 5):
								for num9 in range(1, 5):
									temp = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9
									arr4[temp] += 1

for num1 in range(1, 7):
	for num2 in range(1, 7):
		for num3 in range(1, 7):
			for num4 in range(1, 7):
				for num5 in range(1, 7):
					for num6 in range(1, 7):
						temp = num1 + num2 + num3 + num4 + num5+ num6
						arr6[temp] += 1

total = 0

for i in range(0, 37):
	temp = 0
	for j in range(0, i):
		temp += arr6[j]
	total += temp * arr4[i]

total = total / (4**9 * 6**6)

print(round(total, 7))

# Answer: 0.5731441
