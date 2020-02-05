# Dijkstra's shortest-path algorithm is used.

import math

arr = []

with open("Problem 82 - Path sum three ways.txt") as f:
	for line in f:
		temp = [int(i) for i in line.split(',')]
		arr.append(temp)

count = len(arr)

h = count**2;
vert = [[] for y in range(h)]
length = [[] for y in range(h)]


for x in range(0, count):
	for y in range(0, count):
		# for edges to right
		if (y != count - 1):
			vert[x * count + y].append(x * count + y + 1)
			length[x * count + y].append(arr[x][y + 1])
		# for edges to left
		if (y != 0):
			vert[x * count + y].append(x * count + y - 1)
			length[x * count + y].append(arr[x][y - 1])
		# for edges to downwards
		if (x != count - 1):
			vert[x * count + y].append((x + 1) * count + y)
			length[x * count + y].append(arr[x + 1][y])
		# for edges to upwards
		if (x != 0):
			vert[x * count + y].append((x - 1) * count + y)
			length[x * count + y].append(arr[x - 1][y])
		

visited = [True] * 1 + [False] * (h - 1)
distance = [arr[0][0]] + [math.inf] * (h - 1)

flag = 0
while flag == 0:
	dist = math.inf
	flag = 1
	for v in range(0, h):
		if visited[v] == True:
			len_ind = 0 # length index
			for w in vert[v]:
				if visited[w] == False:
					tmp = distance[v] + length[v][len_ind]
					if tmp < dist:
						flag = 0
						dist = tmp
						min_v = v
						min_w = w
				len_ind += 1
	if flag == 0:
		visited[min_w] = True
		distance[min_w] = dist

print(distance[-1])

# Answer: 425185