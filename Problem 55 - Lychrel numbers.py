def reverse(num):
    temp = 0
    while(num > 0):
        temp *= 10
        temp += (num % 10)
        num = int(num / 10)
    return temp

def Lychrel(num):
    num += reverse(num)
    for i in range(50):
        temp = reverse(num)
        if (temp == num):
            return False
        else:
            num += temp
    return True


total = 0
for i in range(1, 10001):
    if (Lychrel(i) == True):
        total += 1

print(total)

# Answer: 249