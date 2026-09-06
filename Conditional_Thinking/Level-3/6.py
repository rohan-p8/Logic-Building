# Take coordinates (x, y) and determine which quadrant the point lies in.

x = int(input("Enter X coordinate: "))
y = int(input("Enter Y coordinate: "))

if x > 0 and y > 0:
	print(f"\nX = {x} and Y = {y} lies in Top-right section")

elif x < 0 and y > 0:
	print(f"\nX = {x} and Y = {y} lies in Top-left section")

elif x < 0 and y < 0:
	print(f"\nX = {x} and Y = {y} lies in Bottom-left section")

else:
	print(f"\nX = {x} and Y = {y} lies in Bottom-right section")

