#  Print the product of a given number. 

n = int(input("Enter a number: "))
prod = []

for i in range(1, n + 1):
    if n % i == 0:
        prod.append(i)

print(f"Product of {n} are : ", prod)