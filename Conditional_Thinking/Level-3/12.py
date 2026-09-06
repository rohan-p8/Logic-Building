#  Check whether a number is a perfect square (without using the square root function). 

def isSqrt(n):

	if n < 0:
		return False

	if n == 0 or n == 1:
		return True


	low, high = 1, n 

	while low <= high:
		mid = (low + high) // 2

		if mid * mid == n:
			return True

		elif mid * mid < n:
			low = mid + 1

		else:
			high = mid - 1

	return False


	n = int(input("Enter a number: "))

	if isSqrt(n):
		print("True")
	else:
		print("False")


