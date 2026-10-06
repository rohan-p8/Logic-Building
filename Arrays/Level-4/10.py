# Print all elements that appear more than once. 

numbers = [4, 2, 4, 1, 2]

frequency = {}

for num in numbers:

	if num in frequency:
		frequency[num] += 1
	else:
		frequency[num] = 1

duplicate = []

for num, count in frequency.items():
	if count > 1:
		duplicate.append(num)

print(f"\nElements appearing more than once:", duplicate) 

