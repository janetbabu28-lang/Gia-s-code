print("What would you like to eat?")
print("1:Ice cream")
print("2.Pizza")
choice = int(input("Enter your choice - 1 or 2: "))

if (choice == 1):
    print("What flavour would you like?")
    print("1.Chococlate")
    print("2.Vanilla")
    choice2 = int(input("Enter you choice - 1 or 2: "))
    if (choice2 == 1):
        print("Enjoy your chocolate icecream!")
    else:
        print("Enjoy your vanilla ice cream!")
else:
    print("What flavour would you like?")
    print("1.Veg")
    print("2.Non Veg")
    choice3 = int(input("Enter you choice - 1 or 2: "))
    if (choice3 == 1):
        print("Enjoy your veg pizza!")
    else:
        print("Enjoy your non veg pizza!")          