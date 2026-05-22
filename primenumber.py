lower = int(input("Lower range: "))
upper = int (input("Upper range: "))

print("Prime numbers between",lower, "and", upper, "are: ")
num = 0
for num in range(lower,upper+1):
    if num > 1:
        for i in range (2,num):
            if(num%i)==0:
                break

        else:
            print(num)    
    

