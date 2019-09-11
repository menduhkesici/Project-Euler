# for 1
def A(n):
	if n >= 0:
		return 1
	else:
		return 0

# for 2
def B(n):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	else:
		return A(n) + B(n-2)

# for 5
def C(n):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	else:
		return B(n) + C(n-5)

# for 10
def D(n):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	else:
		return C(n) + D(n-10)

# for 20
def E(n):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	else:
		return D(n) + E(n-20)

# for 50
def F(n):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	else:
		return E(n) + F(n-50)

# for 100
def G(n):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	else:
		return F(n) + G(n-100)

# for 200
def H(n):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	else:
		return G(n) + H(n-200)

print(H(200))

# Answer: 73682