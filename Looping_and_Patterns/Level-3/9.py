# Print first n terms of an arithmetic progression (a, d). 

a = int(input("Enter starting number of progression: "))
d = int(input("Enter distance between 2 progression: "))
n = int(input("Enter numbers of times: "))

cur = a

for i in range(n):
	print(cur, end=" ")
	cur += d

