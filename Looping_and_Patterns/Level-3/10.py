# Print first n terms of a geometric progression (a, r). 

a = int(input("Enter starting number: "))
r = int(input("Enter number you multiply by to get the next term: "))
n = int(input("How many no. you want to print: "))

cur = a

for i in range(n):
	# print(cur, end=" ")
	cur = a * (r ** i)
	print(cur, end=" ")

	