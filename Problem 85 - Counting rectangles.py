import math

closest_dist = math.inf
closest_x = 0
closest_y = 0

for max_x in range(1,100):
	for max_y in range(1,100):
		temp = 0
		for x in range(1, max_x + 1):
			for y in range(1, max_y + 1):
				temp += (max_x - x + 1) * (max_y - y + 1)
		if abs(temp - 2 * 10**6) < closest_dist:
			closest_dist = abs(temp - 2 * 10**6)
			closest_x = max_x
			closest_y = max_y
		if temp > 2 * 10**6:
			break

print(closest_x * closest_y)

# Answer: 2772