max_p = 38000
max_h = 28000

cache_p = {}
cache_h = {}

for n in range(166, max_p):
	cache_p[(n * (3 * n - 1) / 2)] = True

for n in range(144,max_h):
	cache_h[(n * (2 * n - 1))] = True

max_p = max_p - 1
max_p = max_p * (3 * max_h - 1) / 2

max_h = max_h - 1
max_h = max_h * (2 * max_h - 1)

max_t = max(max_p, max_h)
flag = 0
t = 286

while True:
	temp = t * (t + 1) / 2
	if (temp > max_t):
		if (max_p < max_h):
			print("increase max_p")
		else:
			print("increase max_h")
		break
	if (temp in cache_h) and (temp in cache_p):
		flag = 1
		print(int(temp))
		break
	t += 1

# Answer: 1533776805