# Check if a number is a palindrome.

n = int(input("Enter a number: "))
temp = n
rev = 0

while temp != 0:
    rem = temp % 10
    rev = rev * 10 + rem
    temp = temp // 10

if n == rev:
    print(f"{n} is Palindrome number")

else:
    print(f"{n} is not Palindrome number")

