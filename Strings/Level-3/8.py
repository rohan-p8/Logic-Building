# Print the second half of the string in reverse. 

str1 = input("Enter string to convert half of string in reverse: ").strip()

length = len(str1)

if length == 0:
	print("\nEmpty string")

else:

	mid = length // 2
	revHalf = ""
	
	for i in range(len(str1) - 1, mid - 1, -1):
		revHalf += str1[i]

	print("\nHalf string in reverse: ",str1[:mid] + revHalf)

