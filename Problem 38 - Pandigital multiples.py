# returns True if the given number is a pandigital number
def isPan(num):
	table = [0] * 10

	while (num > 0):
		temp = num % 10
		if temp == 0:
			return False
		table[temp] += 1
		num = int(num / 10)

	for x in range(1,10):
		if (table[x] != 1):
			return False
	return True

max_val = 0


for x in range(1,100000):
	string = ""
	n = 1
	flag = 0
	while True:
		if (len(string) < 9):
			string += str(x * n)
			n += 1
		elif (len(string) == 9):
			flag = 1
			break
		else:
			break
	if (flag == 1):
		num = int(string)
		if (isPan(num) == True):
			if (num > max_val):
				max_val = num

print(max_val)

# Answer: 932718654