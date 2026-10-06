# Create a frequency list of numbers (count occurrence of each number). 

numbers = [4, 2, 4, 1, 2]

freqMap = {}

for num in numbers:
	if num in freqMap:
		freqMap[num] += 1

	else:
		freqMap[num] = 1

print(freqMap)

