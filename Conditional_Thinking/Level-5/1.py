# Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or at the 
# origin.

x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x == 0 and y == 0:
	print("At the origin")

elif x == 0:
	print("Lies on Y-Axis")

elif y == 0:
	print("Lies on X-Axis")

else:
	print("Does not lies on X or Y Axis")