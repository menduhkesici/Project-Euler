def quickSort(arr):
    less = []
    pivotList = []
    more = []
    arr_length = len(arr)
    if arr_length <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

with open ('Problem 22 - Names scores.txt', 'rt') as myfile:
	a = eval('[' + myfile.read() + ']')

a = quickSort(a)

sumx = 0

for x in range(0,len(a)):
	for y in range(0,len(a[x])):
		sumx += (x+1) * (ord(a[x][y])-64)

print(sumx)

# Answer: 871198282