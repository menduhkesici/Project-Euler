arr = []

with open("Problem 81 - Path sum two ways.txt") as f:
	for line in f:
		temp = [int(i) for i in line.split(',')]
		arr.append(temp)

count = len(arr)

min_val = [[0 for i in range(count)] for i in range(count)]

min_val[0][0] = arr[0][0]

for x in range(0, count):
	min_val[0][x] = arr[0][x] + min_val[0][x - 1]
	min_val[x][0] = arr[x][0] + min_val[x-1][0]

for x in range(1, count):
	for y in range(1, count):
		min_val[x][y] = arr[x][y] + min(min_val[x-1][y], min_val[x][y-1])

print(min_val[-1][-1])

# Answer: 427337