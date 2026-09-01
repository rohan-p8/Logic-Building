# Print Fibonacci series up to n terms.

terms = int(input("Enter a number of terms:"))

n1, n2 = 0, 1
print(n1, end=" ")
print(n2, end=" ")

count = 0

while count < terms:
	res = n1 + n2
	print(res, end=" ")
	
	n1 = n2
	n2 = res
	count += 1


# 2nd way:

# terms = int(input("Enter number of terms: "))

# n1, n2 = 0, 1

# for _ in range(terms):
	
# 	print(n1)
# 	n1, n2 = n2, n1 + n2

	