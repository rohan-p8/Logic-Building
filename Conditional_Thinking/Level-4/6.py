# Take two numbers and check if both are positive and their sum is less than 100. 

num1, num2 = map(int, input("Enter two numbers: ").split())

if num1 > 0 and num2 > 0:

	res = num1 + num2

	if res < 100:
		print(f"\n{num1} and {num2} are positive numbers.\nSum of {num1} + {num2} = {res} less than 100")

	else:
		print(f"\nBoth numbers are positive but addition is {res} greater than 100")

else:
	print("Enter positive numbers only !!")

	