f = [1, 1]
n = 1

while f[n] < 10**999:
	f.append(f[n] + f[n - 1])
	n += 1

print(n+1)

# Answer: 4782