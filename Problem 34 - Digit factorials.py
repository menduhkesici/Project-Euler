f = [1]
for i in range(1, 10):
    f.append(f[i-1] * i)

sumy = 0

for x in range(10,100000):
    z = x
    sumx = 0
    while(z > 0):
        y = z % 10
        z = z // 10
        sumx += f[y]
    if sumx == x:
        sumy += x

print(sumy)

# Answer: 40730