# Take electricity units consumed and calculate the bill as per slabs (using if-else). 

units = int(input("Enter electricity units consumed: "))

if units < 0:
	print("Units cannot be negative")

elif units <= 100:
	bill = units * 5

elif units <= 200:
	bill = (100 * 5) + (units - 100) * 7

else:
	bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print(f"\nTotal electricity bill: ₹{bill}")

