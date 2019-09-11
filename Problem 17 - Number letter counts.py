# x <= 999
def count_letters(x):
	total = 0

	if x == 0:
		return total

	# first digit
	a = x % 10

	total = total + val_first(a)

	if x < 10:
		return total

	# second digit
	b = (x // 10) % 10

	if b == 1:
		total = val_third(a)
	else:
		total = total + val_second(b)

	if x < 100:
		return total

	# third digit
	c = (x // 100) % 10

	total = total + val_first(c) + 10

	# 'and' is not used when last two digits are zeroes.
	if a == 0 and b == 0:
		total = total - 3

	return total

# for first digit
def val_first(argument):
	switcher = {
		0: 0,
		1: 3,
		2: 3,
		3: 5,
		4: 4,
		5: 4,
		6: 3,
		7: 5,
		8: 5,
		9: 4,
	}
	return switcher.get(argument, "nothing")

# for second digit (when it is not 1)
def val_second(argument):
	switcher = {
		0: 0,
		2: 6,
		3: 6,
		4: 5,
		5: 5,
		6: 5,
		7: 7,
		8: 6,
		9: 6,
	}
	return switcher.get(argument, "nothing")

# for sum of first and second digit (when second digit is 1)
def val_third(argument):
	switcher = {
		0: 3,
		1: 6,
		2: 6,
		3: 8,
		4: 8,
		5: 7,
		6: 7,
		7: 9,
		8: 8,
		9: 8,
	}
	return switcher.get(argument, "nothing")

letters = 0

for x in range(1,1000):
	letters += count_letters(x)

print(letters + 11)

# Answer: 21124