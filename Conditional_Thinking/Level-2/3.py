# Take marks (0–100) and print the corresponding grade (A/B/C/D/Fail)

marks = int(input("Enter marks (0-100): "))

if marks <= 0 or marks > 100:
    print("Invalid marks !!!")

else:

    if marks >= 90 and marks <= 100:
        print("Grade A")

    elif marks >= 80 and marks <= 89:
        print("Grade B")

    elif marks >= 60 and marks <= 79:
        print("Grade C")

    elif marks >= 40 and marks <= 59:
        print("Grade D")

    else:
        print("Fail")

    