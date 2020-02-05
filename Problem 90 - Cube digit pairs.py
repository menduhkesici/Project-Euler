import itertools

lst = list(range(0, 10))

comb = list(itertools.combinations(lst, 6))

total = 0

for x in range(0, len(comb)):
	for y in range(x + 1, len(comb)):

		cube1 = comb[x]
		cube2 = comb[y]

		flag = 1
		if ((0 in cube1 and 1 in cube2) or (1 in cube1 and 0 in cube2)) == False:
			flag = 0
		if ((0 in cube1 and 4 in cube2) or (4 in cube1 and 0 in cube2)) == False:
			flag = 0
		if ((0 in cube1 and 9 in cube2) or (9 in cube1 and 0 in cube2) or (0 in cube1 and 6 in cube2) or (6 in cube1 and 0 in cube2)) == False:
			flag = 0
		if ((1 in cube1 and 6 in cube2) or (6 in cube1 and 1 in cube2) or (1 in cube1 and 9 in cube2) or (9 in cube1 and 1 in cube2)) == False:
			flag = 0
		if ((2 in cube1 and 5 in cube2) or (5 in cube1 and 2 in cube2)) == False:
			flag = 0
		if ((3 in cube1 and 6 in cube2) or (6 in cube1 and 3 in cube2) or (3 in cube1 and 9 in cube2) or (9 in cube1 and 3 in cube2)) == False:
			flag = 0
		if ((6 in cube1 and 4 in cube2) or (4 in cube1 and 6 in cube2) or (9 in cube1 and 4 in cube2) or (4 in cube1 and 9 in cube2)) == False:
			flag = 0
		if ((8 in cube1 and 1 in cube2) or (1 in cube1 and 8 in cube2)) == False:
			flag = 0

		if (flag == 1):
			total += 1


print(total)

# Answer: 1217