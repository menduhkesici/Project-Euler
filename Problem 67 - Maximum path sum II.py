arr = []
count = 0

with open("Problem 67 - Maximum path sum II.txt") as f:
	for line in f:
		temp = [int(i) for i in line.split()]
		arr.append(temp)
		count += 1

max_val = [[0 for i in range(count)] for i in range(count)]

max_val[0][0] = arr[0][0]

for x in range(1, count):
	max_val[x][0] = arr[x][0] + max_val[x-1][0]

for x in range(1, count):
	max_val[x][x] = arr[x][x] + max_val[x-1][x-1]

for x in range(2, count):
	for y in range(1, x):
		max_val[x][y] = arr[x][y] + max(max_val[x-1][y-1], max_val[x-1][y])

print(max(max_val[count-1]))

# Answer: 7273