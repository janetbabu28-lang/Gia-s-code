math = int(input("Enter your math score: "))
english = int(input("Enter your english score: "))
science = int(input("Enter your science score: "))
hindi = int(input("Enter your hindi score: "))

sum = math+english+science+hindi
print("Your total score is: ",sum)
perc = (sum/400)*100
print("Your overall percentage is: ",perc)