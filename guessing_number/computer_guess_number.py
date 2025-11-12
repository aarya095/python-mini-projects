import random

def computer_guess_our_number(high):

    feedback = ''
    computer_guess = None

    low = int(input("What number you like to be the lower limit -> "))
    high = int(input("What number you like to be the higher limit -> "))
    user_number = int(input("Please provide your secret number -> "))

    # verifying validity of lower and higher limits provided by the user 
    if high == low + 1:
        print("\nPlease provide the computer a range of numbers to guess over.")
        exit()
    elif low > high:
        print("\nYou have inputted lower limit greater than higher limit, please input lower limit lesser than higher limit.")
        exit()
    elif low == high:
        print("\nYou have inputted lower limit equal to higher limit, please input lower limit lesser than higher limit.")
        exit()

    # verifying validity of secret number provided by the user
    if user_number < low or user_number > high:
        print("\nPlease provide a number in lower and higher limit.")
        exit()

    while computer_guess != user_number:
        if low < high:
            computer_guess = random.randint(low, high)
            print(f"\nComputer guess the following number: {computer_guess}")
            feedback = input("'h' for high, 'l' for low, 'c' for correct: ").lower()
            
            if (feedback != 'h') and (feedback != 'l') and (feedback != 'c'):
                print("Please provide a requested letter.")

            if feedback == 'h':
                high = computer_guess - 1
            if feedback == 'l':
                low = computer_guess + 1
            if feedback == 'c':
                exit()
        elif low > high:
            print("You have missed the number and computer has already guessed it!")
            exit()
        elif low == high:
            computer_guess = low # also can be high b/c high = low


    print(f"\nYour number is {computer_guess}. \nYay! The computer was able to guess your number!")

computer_guess_our_number(5)