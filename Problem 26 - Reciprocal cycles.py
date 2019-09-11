maxx = 0
index = 0

for x in range(2,1000):
	arr = [0]
	y = 10
	z = x
	while y % z not in arr:
		arr.append(y % z)
		y = (y % z) * 10
	if y % z == 0:
		k = 0
	else:
		k = len(arr) - arr.index(y % z)
	if k > maxx:
		maxx = k
		index = x

print(index)

# Answer: 983