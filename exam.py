medical_cause = input("Please enter medical cause, Yes or No, Y or N : ")
attendance = int(input("Enter your attendance: "))

if medical_cause == "Y":
    print("Allowed to sit for exam")
else:
    if attendance >= 75:
        print("Allowed to sit for the exam")
    else:
        print("You are not allowed to enter the exam")            
