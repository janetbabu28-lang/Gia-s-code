number = int(input("Enter a number: "))
count = 0

i = number
while i > 0:
    count = count+1
    i = i//10
print("The number of digits is,",count)        