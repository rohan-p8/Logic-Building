# Take a weekday number (1–7) and determine if it is a weekday or weekend.

weekday = input("Enter weekday number (1-7): ")

weeks = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

for i in range(1, len(weekday) + 1):

	# if len(weekday) == 1 and weekday.isdigit():

	# 	print(weeks[int(weekday)])
	# 	break;
	print(weeks[i])


