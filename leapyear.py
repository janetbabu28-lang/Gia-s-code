year = int(input("Enter year: "))

if year % 4 ==0:
    print("Leap year")
else:
    print("Not a leap year") 

age = int(input("Enter your age: "))

if age <=17:
    print("Not eligible to vote")
else:
    print ("eligible to vote")         