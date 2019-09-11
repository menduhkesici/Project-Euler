largest_number = 0

for x in range(100,1000):
	for y in range(x,1000):
		Number_0 = Number = x * y

		if Number > largest_number:
			Reverse = 0

			while(Number > 0):
				Reminder = Number % 10
				Reverse = (Reverse * 10) + Reminder
				Number = Number // 10

			if Number_0 == Reverse:
				largest_number = Number_0

print(largest_number)

# Answer: 906609