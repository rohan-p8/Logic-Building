# Print the reverse of a given number.

n = int(input("Enter a number: "))
revNo = 0

while n != 0:
    rem = n % 10
    revNo = revNo * 10 + rem
    n = n // 10


print(revNo)

