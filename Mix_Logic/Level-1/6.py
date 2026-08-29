# Count how many even digits a number contains. 

n = int(input("Enter a number: "))
even = 0

while n != 0:
    rem = n % 10

    if rem % 2 == 0:
        even += 1

    n = n // 10

print(f"Count of Even digits: {even}")

