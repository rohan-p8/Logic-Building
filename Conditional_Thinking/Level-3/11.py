#  Check whether a number is a perfect square (without using the square root function). 
import math

def isPerfectSquare(n):

	if n < 0:
		return False

	else:
		root = int(math.sqrt(n))


	return root * root == n


n = int(input("Enter number to check perfect square: "))

if isPerfectSquare(n):
	print("True")
else:
	print("False")

