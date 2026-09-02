# Find the count of prime numbers in the list

list1 = [2,3,4,5,6,7,11,12,20,13,41]

print("Given list: ",list1)

count = 0

for num in list1:
	for i in range(2, num):
		if num % i == 0:
			break
	else:
		count += 1

print(f"\nCount of prime numbers: {count}")


    