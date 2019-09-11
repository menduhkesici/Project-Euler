LastNumber = 1 + 20
Number = 1

for x in range(1,LastNumber):
	gcd = 1
	y = x
	
	while y > 0:
		if (Number % y == 0) and (x % y == 0):
			gcd = y
			break
		y = y - 1

	Number = Number * x / gcd

print (Number)

# Answer: 232792560