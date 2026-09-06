# Take two angles of a triangle and compute the third angle. 

a1 = int(input("Enter angle 1: "))
a2 = int(input("Enter angle 2: "))

print(f"\nFirst angle: {a1}")
print(f"Second angle: {a2}")

if a1 and a2 > 0:

	a3 = abs((a1 + a2) - 180)

	print(f"\nThird angle is: {a3}")

else:
	print("\nEnter valid angle value")

