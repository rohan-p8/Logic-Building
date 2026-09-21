# Take a weekday number (1–7) and determine if it is a weekday or weekend.

weekday = input("Enter weekday number (1-7): ").strip()

if weekday in {"1","2","3","4","5"}:
	print("\nWeekday")

elif weekday in {"6","7"}:
	print("\nWeekend")

else:
	print("\nEnter valid weekday number (1-7)")

	