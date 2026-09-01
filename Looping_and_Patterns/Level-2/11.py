#  Print sum of first n terms of Fibonacci series

terms = int(input("Enter terms: "))

arr = []
n1, n2 = 0, 1

for _ in range(terms):
	arr.append(n1)
	n1, n2 = n2, n1 + n2

print(arr)

n = int(input("Enter no. of terms sum you want: "))

total_sum = sum(arr[:n])

print(total_sum)


