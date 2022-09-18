# text to num converter
def text_to_num(text):
	total = 0
	for x in range(0,len(text)):
		total += ord(text[x]) - ord('A') + 1
	return total


with open("Problem 42 - Coded triangle numbers.txt") as f:
	arr = eval("[" + f.read() + "]")

cache = {}
for x in range(1,30):
	temp = x * (x + 1) / 2
	cache[temp] = True

total = 0
for word in arr:
	if (text_to_num(word) in cache):
		total += 1

print(total)

# Answer: 162