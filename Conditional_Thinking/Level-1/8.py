# Take a temperature value and print “Cold”, “Warm”, or “Hot” 
# using range conditions.

temp = float(input("Enter temperature: "))

if temp <= 10.00:
    print("There is Cold Temperature")

elif temp >= 10.01 and temp <= 25.00:
    print("There is Warm Temperature")

else:
    print("There is Hot Temperature")

