# Check if a number is palindrome (121 → true). 

n = int(input("Enter no. to check Palindrome or not: "))
temp = n

reverse = 0

while temp != 0:
	rem = temp % 10
	reverse = reverse * 10 + rem
	temp = temp // 10

if reverse == n:
	print(f"\n{n} is Palindrome")
else:
	print(f"\n{n} is not Palindrome")