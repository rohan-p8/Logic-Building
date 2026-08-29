# If the sides form a valid triangle, determine whether it is equilateral, isosceles, or 
# scalene

s1 = int(input("Enter first side of triangle: "))
s2 = int(input("Enter second side of triangle: "))
s3 = int(input("Enter third side of triangle: "))

triangle = s1 + s2 + s3

if triangle == 180:
    print("\nValid Triangle")
    print("Sum of angles: ", triangle)

    if s1 == 60 and s2 == 60 and s3 == 60:
        print("\nEquilateral Triangle")
    elif (s1 == 60 and s2 == 60) or (s1 == 60 and s3 == 60) or (s2 == 60 and s3 == 60):
        print("\nIsosceles Triangle")
    else:
        print("\nScalne Triangle")

else:
    print("\nNot a valid triangle")
    print("Sum of angles: ", triangle)

