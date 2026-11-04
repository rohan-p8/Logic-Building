# Take three numbers and check if they can form a Pythagorean triplet.

a, b, c = map(int, input("Enter three numbers: ").split())

smaller = sorted([a, b, c])

s1 = smaller[0]
s2 = smaller[1]
s3 = smaller[2]

res = (s1 ** 2) + (s2 ** 2)

if res == s3 ** 2:
	print(f"\n{a, b, c} are pythagorean triplet")

else:
	print("\nNot pythagorean triplet")