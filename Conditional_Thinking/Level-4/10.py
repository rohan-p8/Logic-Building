# Take a password string and check basic rules (length ≥ 8 and contains at least one 
# digit).

password = input("Enter password: ")

if len(password) >= 8:

	for char in password:
		if char.isdigit():
			print("Password is valid")
			break;

	else:
		print("Password must contain at least one digit")

else:
	print("Password length must be at least 8 characters")

	