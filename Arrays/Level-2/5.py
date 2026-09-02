# Check if all elements in the list are unique. 

list1 = [12,55,38,9,89]

print("Given list: ",list1)

seen = set()

for item in list1:
	if item in seen:
		print("Not Unique")
		break
	else:
		seen.add(item)
		print("Unique")
		break




# using set():

# s1 = set(list1)

# if len(list1) == len(s1):
# 	print("Unique elements are in list")
# else:
# 	print("Not unique")

