# Check if a number is a strong number (sum of factorials of digits = number). 

n = int(input("Enter a number to check it is strong or not: "))
temp = n
sumFact = 0

while temp > 0:
	digit = temp % 10

	fact = 1
	for i in range(1, digit + 1):
		fact = fact * i

	sumFact += fact
	temp = temp // 10

if sumFact == n and n > 0:
	print(f"\n{n} is Strong Number")

else:
	print(f"\n{n} is NOT a Strong Number")

