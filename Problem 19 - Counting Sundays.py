months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

x = 1
total = 0

for a in range(1901,2001):
	for b in range(0,12):
		if x % 7 == 1:
			total += 1
		x += months[b]
		if (a % 4 == 0) and (b == 1):
			x += 1
		
print(total)

# Answer: 171