num = input("Please enter your number: ")
length = len(num)
if length % 2 == 1:
    middle = int(num[length// 2])
    product = middle
else:
    middle1=int(num[length//2-1])
    middle2=int(num[length//2])
    product = middle1*middle2
print("The total product of your middle numbers is: ",product)   