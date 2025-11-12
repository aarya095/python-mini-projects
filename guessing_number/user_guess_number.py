import random

def guess_random_number(x):
    random_number = random.randint(1,x)
    user_guess = -1 # this value can be anything less than 1.

    while user_guess != random_number:
        user_guess = int(input("Try and Guess the number: "))

        if user_guess > random_number:
            print("Too High! Try again.")
        elif user_guess < random_number:
            print("Too Low! Try again.")
        
    print("Yay! You have correctly guessed the number!")

guess_random_number(10)