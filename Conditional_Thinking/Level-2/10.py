#  Take a month number (1–12) and print the number of days in that month (ignore leap 
# years).

month = int(input("Enter a month (1-12): "))

bigM = [1,3,5,7,8,10,12]
smallM = [4,6,9,11]
feb = 2

if month in bigM:
    print("31 days")

elif month in smallM:
    print("30 days")

elif month == feb:
    print("28/29 days")

else:
    print("Enter valid month !!!")
    
