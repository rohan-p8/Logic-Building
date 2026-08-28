# Check if a number is an Armstrong number.


n = int(input("Enter a number: "))

power = len(str(n))
result = 0

temp = n

while(temp > 0):
    rem = temp % 10
    result = result + rem ** power
    temp = temp // 10

if n == result:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")

