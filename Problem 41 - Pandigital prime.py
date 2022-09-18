# A number is divisible by 3 if the digit sum of the number is divisible by 3.
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36
# 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
# 1 + 2 + 3 + 4 + 5 + 6 = 21
# 1 + 2 + 3 + 4 + 5 = 15
# 1 + 2 + 3 + 4 = 10
# 1 + 2 + 3 = 6
# 1 + 2 = 3
# From the above list it can be seen that the prime and pandigital number
# can be 7 or 4 digits as other digit sums of other options are divisible by 3.

def isPrime(n):
	for x in range(2, int(n**0.5) + 1):
		if n % x == 0:
			return False # NOT prime number
	return True # prime number

# returns True if the given number is a pandigital number in its base
def isPan(num):
	string = str(num)
	table = [0] * 10

	while (num > 0):
		temp = num % 10
		if temp == 0:
			return False
		table[temp] += 1
		num = int(num / 10)

	for x in range(1,len(string) + 1):
		if (table[x] != 1):
			return False
	return True

for x in range(7654321, -1, -1):
	if (isPan(x) == True):
		if (isPrime(x) == True):
			print(x)
			break

# Answer: 7652413