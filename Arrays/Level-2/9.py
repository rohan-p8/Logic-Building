# Count how many numbers are divisible by 3 and 5 both.

list1 = [14,12,90,120,56,21,25,15,30,60]

print("Given List: ",list1)

count = 0

for num in list1:
	if num % 3 == 0 and num % 5 == 0:
		count += 1
	else:
		pass

if count > 0:
	print(f"\nCount of numbers that are divisible by 3 and 5 is {count}")
else:
	print(f"There are 0 numbers are divisible by both 3 and 5")

