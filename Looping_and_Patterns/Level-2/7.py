# Print all Armstrong numbers between 1 and 1000

for i in range(1, 1001):
    temp = i
    power = len(str(i))
    result = 0

    while temp > 0:
        rem = temp % 10
        result = result + rem ** power
        temp = temp // 10

    if result == i:
        print(i)


        