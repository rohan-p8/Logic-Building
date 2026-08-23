no = int(input("Enter number: "))

if no % 3 == 0 and no % 5 == 0:
    print(f"{no} is divisible by both 3 and 5")
elif no % 3 == 0:
    print(f"{no} is only divisible by 3")
elif no % 5 == 0:
    print(f"{no} is only divisible by 5")
else:
    print(f"{no} is not divisible by both 3 and 5")