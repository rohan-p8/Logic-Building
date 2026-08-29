# Take three sides and check if they form a valid triangle.

a = int(input("Enter first side of triangle: "))
b = int(input("Enter second side of triangle: "))
c = int(input("Enter third side of triangle: "))

triangle = a + b + c

if triangle == 180:
    print("\nValid Triangle")
    print("Sum of angles: ", triangle)
else:
    print("Not a valid triangle")
    print("Sum of angles: ", triangle)

    