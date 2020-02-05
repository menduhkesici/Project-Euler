# convert list of chars to a string
def convert(s):
    new = ""
    for x in s:
        new += x
    return new

cipher = []
with open("Problem 59 - XOR decryption.txt") as f:
    for line in f:
        cipher += [int(i) for i in line.split(',')]

text_file = open("Output.txt", "w")

for i in range(ord('a'), ord('z') + 1):
    for j in range(ord('a'), ord('z') + 1):
        for k in range(ord('a'), ord('z') + 1):
            key = [i, j, k]
            temp = []
            for n in range(len(cipher)):
                char = chr(cipher[n] ^ key[n % 3])
                temp.append(char)
            text_file.write(str(i))
            text_file.write(" ")
            text_file.write(str(j))
            text_file.write(" ")
            text_file.write(str(k))
            text_file.write("\n")
            text_file.write(convert(temp))
            text_file.write("\n")

text_file.close()

# After checking the text file which includes all the possibilities,
# or searching for some common words (such as "the"),
# i, j and k values are found as below.
# i = 101, j = 120, k = 112
# by inserting them, the text can be deciphered.

i = 101
j = 120
k = 112
key = [i, j, k]
temp = []
for n in range(len(cipher)):
    char = chr(cipher[n] ^ key[n % 3])
    temp.append(char)

#print(convert(temp))

total = 0
for n in range(len(temp)):
    total += ord(temp[n])

print(total)

# Answer: 129448
