costprice = int(input("Enter the cost of item bought: "))
sellingprice = int(input("Enter the price of item sold for: "))

outcome = sellingprice - costprice
print("Your outcome is:",outcome)
if outcome > costprice:
    print("You have made a profit")
else:
    print("You have made a loss")