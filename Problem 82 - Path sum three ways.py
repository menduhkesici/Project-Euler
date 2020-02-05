import math

arr = []

with open("Problem 82 - Path sum three ways.txt") as f:
	for line in f:
		temp = [int(i) for i in line.split(',')]
		arr.append(temp)

count = len(arr)

min_val = [[math.inf for i in range(count)] for i in range(count)]

for x in range(0, count):
	min_val[x][0] = arr[x][0]

for y in range(1, count):
	for n in range(count + 1):
		for x in range(0,count):
			if (x == 0):
				min_val[x][y] = arr[x][y] + min(min_val[x][y-1], min_val[x+1][y])
			elif (x == count - 1):
				min_val[x][y] = arr[x][y] + min(min_val[x][y-1], min_val[x-1][y])
			else:
				min_val[x][y] = arr[x][y] + min(min_val[x][y-1], min_val[x-1][y], min_val[x+1][y])
			
min_val_overall = math.inf
for x in range(0, count):
	if (min_val[x][-1] < min_val_overall):
		min_val_overall = min_val[x][-1]

print(min_val_overall)

# Answer: 260324