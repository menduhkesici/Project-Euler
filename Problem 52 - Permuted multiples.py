def foo(num):

	arr = [num]

	string = [""] * 7
	string[1] = str(num)
	length = len(string[0])

	for x in range(2,7):
		temp = x * num
		string[x] = str(temp)
		if (len(string[x]) != len(string[1])):
			return False
		arr.append(temp)

	table = [[0] * 10 for i in range(6)]

	count = 0
	for num in arr:
		while (num > 0):
			temp = num % 10
			if temp == 0:
				return False
			table[count][temp] += 1
			num = int(num / 10)
		count += 1

	for x in range(1,6):
		for y in range(1,10):
			if (table[x][y] != table[0][y]):
				return False

	return True

num = 1
while True:
	if (foo(num) == True):
		print(num)
		break
	num += 1

# Answer: 142857