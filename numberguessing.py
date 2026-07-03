import random
number = random.randint(1,10)
guess = 0

print ("Welcome to the number Guessing Game!")
print("I have chosen a number between 1 and 10.")
while guess != number:
    guess = int(input("Enter your guess: "))
    if guess < number:
        print("too low!")
    elif guess > number:
        print("too high!")
    else:
        print("Congrats! You guessed the number :)")    
        