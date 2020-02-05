# Sieve of Eratosthenes method is used
def isPrime(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1

    temp1 = []
    temp2 = []
    for i in range(2, len(prime)):
        if prime[i] == True:
            temp1.append(i)
        if prime[i] == False:
            temp2.append(i)
    return temp1, temp2

max_n = 10**6
arr_of_primes, arr_of_non_primes = isPrime(max_n)

# Euler's product formula is used to calculate the totient of the number.
# it is true for non-prime numbers. For prime numbers, it is (num - 1).
def totient(num):
    temp = num
    for i in arr_of_primes:
        if (i > (num / 2 + 1)):
            break
        if (num % i == 0):
            temp *= (1 - 1 / i)
    return int(temp)

max_ratio = 0
max_val = 0

for n in arr_of_primes:
    temp = n - 1
    if (n / temp) > max_ratio:
        max_ratio = n / temp
        max_val = n

for n in arr_of_non_primes:
    if (n % 10000 == 0):
        print(n)
    temp = totient(n)
    if (n / temp) > max_ratio:
        max_ratio = n / temp
        max_val = n

print(max_val)

# Answer: 510510