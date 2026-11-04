# Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or at the 
# origin.

x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x == 0 and y == 0:
	print("\nAt the origin")

elif y == 0:
	print("\nOn the X-Axis")

elif x == 0:
	print("\nOn the Y-Axis")

else:
	print("\nNeither axis (lies in a quadrant)")

