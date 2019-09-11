import random

w, h = 15, 15;

vert = [[0 for x in range(w)] for y in range(h)] 

x = 0

with open('Problem 18 - Maximum path sum I.txt') as f:
	for line in f:
		int_list = [int(i) for i in line.split()]
		vert[x] = int_list
		x = x + 1

max_sum = 0

for x in range(1,2**16+1):
	cur_sum = 75
	a = 0
	for y in range(1,15):
		a += random.randint(0,1)
		cur_sum += vert[y][a]
	if max_sum < cur_sum:
		max_sum = cur_sum	

print(max_sum)

# Answer: 1074