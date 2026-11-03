# Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or at the 
# origin.

x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x == 0 and y == 0:
	print("At the origin")

elif x >= 1 and (y > 0 or y < 0):
	print("At X-Axis")

elif x < 0 and (y > 0 or y < 0):
	print("At Y-Axis")

else:
	print("Neither axis")