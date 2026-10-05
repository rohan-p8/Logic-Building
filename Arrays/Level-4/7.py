# Find element-wise sum of two lists (A[i] + B[i]).

lst1 = [1,34,88,63]
lst2 = [15,3,8,18]

add = 0
newLst = []

if len(lst1) != len(lst2):
	print("Length should be same for sum")

else:
	for i in range(len(lst1)):
		add = lst1[i] + lst2[i]
		
		newLst.append(add)

print(newLst)
