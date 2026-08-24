# Print the sum of all even numbers up to n. 

n = int(input("Enter a number: "))
sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sum = sum + i

print(f"Sum of all even no. up to {n} is: ", sum)