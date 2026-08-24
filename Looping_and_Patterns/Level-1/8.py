# Print the sum of all odd numbers up to n.

n = int(input("Enter a number: "))
sum = 0

for i in range(1, n + 1):
    if i % 2 == 1:
        sum += i

print(f"Sum of all odd numbers up to {n} is: ", sum)