# increase max_n until the correct answer is found.

import math

cache = {}

max_n = 10000

for n in range(1, max_n):
	temp = n * (3 * n - 1) / 2
	cache[temp] = True

min_dist = math.inf

for j in range(1, max_n):
	pj = j * (3 * j - 1) / 2
	for k in range((j + 1), (max_n + 1)):
		pk = k * (3 * k - 1) / 2
		if ((pk + pj) in cache) and ((pk - pj) in cache):
			if ((pk - pj) < min_dist):
				min_dist = (pk - pj)

print(int(min_dist))

# Answer: 5482660