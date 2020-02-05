# space efficient method, returns only the primeness information of the given value
def isPrime(n):
	for x in range(2, int(n**0.5) + 1):
		if n % x == 0:
			return 0 # NOT prime number
	return 1 # prime number

temp = 1
ratio = 1
count = 0
num_of_primes = 0
total_num = 1
side_length = 1

while(ratio >= 0.1):
    count += 2
    for i in range(4):
        temp += count
        num_of_primes += isPrime(temp)
    side_length += 2
    total_num += 4
    ratio = num_of_primes / total_num

print(side_length)

# Answer: 26241