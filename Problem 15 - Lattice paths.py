w, h = 21, 21;

grid = [[0 for x in range(w)] for y in range(h)] 

grid[0][0] = 1

for x in range(1,21):
	grid[0][x] = 1
	grid[x][0] = 1

for x in range(1,21):
	for y in range(1,x+1):
		grid[x][y] = grid[x][y-1] + grid[x-1][y]
		grid[y][x] = grid[x][y]

for x in range(0,21):
	print(grid[x])

# Answer: 137846528820