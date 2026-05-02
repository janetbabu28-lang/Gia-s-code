math = int(input("Enter your math score: "))
english = int(input("Enter your english score: "))
science = int(input("Enter your science score: "))
hindi = int(input("Enter your hindi score: "))
geography = int(input("Enter your geography score: "))

total = math+english+science+hindi+geography
avg = total/5

if avg >= 91 and avg <= 100:
    print("Your grade is A1")
elif avg >=81 and avg <=90:
    print("Your grade is A2")    
elif avg >=71 and avg <=80:
    print("Your grade is B3")
elif avg >= 61 and avg <=70:
    print("Your grade is B4")
elif avg >=51 and avg <=60:
    print("Your grade is C5")
elif avg >=41 and avg <=50:
    print("Your grade is C6")
elif avg >=31 and avg <=40:
    print("Your grade is D7")
elif avg >=21 and avg <=30:
    print("Your grade is D8")
else:
    print("Your grade is F9")    
     
 
    
  
        
        
        
        
       

