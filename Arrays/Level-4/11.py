# Sort list elements by their frequency in descending order.

numbers = [4, 2, 4, 1, 2, 3, 3, 3]

frequency = {}

for num in numbers:
	if num in frequency:
		frequency[num] += 1
	else:
		frequency[num] = 1

res = {k:v for k,v in sorted(frequency.items(), key=lambda item: item[1], reverse=True)}

print(f"\nElements by their frequency in descending order: {res}")
