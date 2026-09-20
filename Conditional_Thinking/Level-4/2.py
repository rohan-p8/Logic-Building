# Take a number and print “Fizz” if divisible by 3, “Buzz” if divisible by 5, and 
# “FizzBuzz” if divisible by both. 

num = int(input("Enter number: "))

if num % 3 == 0 and num % 5 == 0:
	print("\nFizzBuzz")

elif num % 3 == 0:
	print("\nFizz")

elif num % 5 == 0:
	print("\nBuzz")

else:
	print(f"\n{num} is not divisible by 3 or 5 !!!")

	