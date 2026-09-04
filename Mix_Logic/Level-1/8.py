# Print the reverse of a number (123 → 321). 

n = int(input("Enter no. to reverse: "))
print(f"Reverse of given {n} is: ")
res = 0

while n != 0:
	rem = n % 10 
	res = res * 10 + rem
	n = n // 10

print(f"Reverse: ",res)

