# Check if an amount can be evenly divided into 2000, 500, and 100 currency notes

amount = int(input("Enter amount: "))

if amount > 0:

	if amount % 2000 == 0:
		print("Amount divides evenly by 2000,500 or 100")
	else:
		res = amount // 2000
		rem = amount - res * 2000

		if rem % 500 == 0:
			print("Amount divides evenly by 2000,500 or 100")
		else:
			res1 = rem // 500
			rem1 = rem - res1 * 500

			if rem1 % 100 == 0:
				print("\nAmount divides evenly by 2000,500 or 100")
				print("2000 * ",res)
				print("500 * ",res1)
				print("100 * ",rem1 // 100)
			else:
				print("\nAmount Not divides evenly by 2000,500 and 100 notes")

else:
	print("Enter valid amount")

