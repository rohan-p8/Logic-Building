# Check if a number is an Armstrong number

n = int(input("Enter a number: "))
temp = n
power = len(str(n))
res = 0

while temp > 0:
    rem = temp % 10
    res = res + rem ** power
    temp = temp // 10

if n == res:
    print(f"{n} is an Armstrong number")

else:
    print(f"{n} is not an Armstrong number")


