# Print all numbers between a and b divisible by 7.

a, b = map(int, input("Enter a and b range to find numbers divisible by 7: ").split())

if a <= 0 or b <= 0 or a >= b:
	print("Enter valid range !!!")

else:
	for i in range(a, b + 1):
		if i % 7 == 0:
			print(f"{i} is divisible by 7")


