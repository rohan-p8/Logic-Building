# Take three numbers and print the median value (neither maximum nor minimum)

a, b, c = map(int, input("Enter three numbers to find median: ").split())

if b <= a <= c or c <= a <= b:
	print(f"\n{a} is median")

elif a <= b <= c or c <= b <= a:
	print(f"\n{b} is median")

else:
	print(f"\n{c} is median")

