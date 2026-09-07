# Find LCM of two numbers using loops. 

n1, n2 = map(int, input("Enter two numbers to find LCM: ").split())
min_num = min(n1, n2)

for i in range(min_num, 0, -1):
	if n1 % i == 0 and n2 % i == 0:
		lcm = (n1 * n2) // i
		print(f"\nLCM of {n1} and {n2} is: {lcm}")
		break

