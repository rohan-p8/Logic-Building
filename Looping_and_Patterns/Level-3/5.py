# Find LCM of two numbers using loops. 

n1, n2 = map(int, input("Enter two numbers to find LCM: ").split())
min_num = min(n1, n2)

for i in range(min_num, 0, -1):
	if n1 % i == 0 and n2 % i == 0:
		lcm = (n1 * n2) // i
		print(f"\nLCM of {n1} and {n2} is: {lcm}")
		break
	

# Find LCM Without finding HCF first

# n1, n2 = map(int, input("Enter two numbers to find LCM: ").split())

# # Start from the larger number and step by that number
# step = max(n1, n2)
# multiple = step

# while True:
#     if multiple % n1 == 0 and multiple % n2 == 0:
#         print(f"\nLCM of {n1} and {n2} is: {multiple}")
#         break
#     multiple += step