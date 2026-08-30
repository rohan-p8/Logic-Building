# Take the hour of the day (0–23) and print “Good Morning”, “Good Afternoon”, “Good 
# Evening”, or “Good Night”.

hour = int(input("Enter hours (0-23): "))

if hour <= 0 or hour > 23:
    print("Invalid Hours !!!")

else:

    if hour > 0 and hour <=11:
        print("Good Morning");

    elif hour >= 12 and hour <= 16:
        print("Good Afternoon")

    elif hour >= 17 and hour <= 19:
        print("Good Evening")

    else:
        print("Good Night")
