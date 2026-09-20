# Take income and age, and check if eligible for tax (age > 18 and income > 5 L).

income = int(input("Enter income per annum: "))
age = int(input("Enter age: "))

if age >= 18 and income >= 500000:
	print("\nEligible for tax")

else:
	print("\nNot eligible for tax")

	