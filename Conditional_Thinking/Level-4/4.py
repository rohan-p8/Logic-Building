# Take 24-hour time (hours and minutes) and print whether it is AM or PM.

hours, minutes = map(int, input("Enter hours and minutes: ").split())

if 0 <= hours <= 23 and 0 <= minutes <= 59:

	if hours < 12:
		print("AM")

	else:
		print("PM")

else:
	print("\nEnter valid time !!")

