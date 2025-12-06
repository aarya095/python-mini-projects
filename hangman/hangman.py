# Hangman game
"""
computer will select a word from a predefined list of words. 
"""
# Built-in Modules
import random

# User-defined modules
from words import words

correct_guessed_letters_list = []
already_guessed_letters_set = set() # consists of both correct guesses and incorrect guesses
selected_word_letters_list = []

def select_random_word():
    """Selects a random word"""

    x = random.choice(words)
    return x 

def convert_str_to_list_of_words(randomly_selected_word):
    """Converst string to list of letters"""

    for letter in randomly_selected_word:
        selected_word_letters_list.append(letter)

    return selected_word_letters_list

def create_list_to_store_guessed_letters(selected_word_letters_list):
    """Create a dynamic list of dashes(-) to display for user to see"""

    for i in range(0,len(selected_word_letters_list)):
        correct_guessed_letters_list.append('-')
    print(*correct_guessed_letters_list)

    return correct_guessed_letters_list

def count_num_of_letters(list, letter):
    """Count number of letters in the word"""

    num_of_letter = 0
    for i in list:
        if i == letter:
            num_of_letter = num_of_letter + 1
    
    return num_of_letter

def play_hangman(correct_guessed_letters_list):

    # Loop till having '-' in the correct_guessed_letters_list
    while '-' in correct_guessed_letters_list:

        user_guess = input("Please guess a letter: ").strip().lower()

        # Display already used letters and displays if the list is not empty
        if len(already_guessed_letters_set) != 0:
            print(f"Already used letters: {already_guessed_letters_set}")

        # Checks if the user has already guessed the letter
        if user_guess in correct_guessed_letters_list or \
                user_guess in already_guessed_letters_set:
            already_guessed_letters_set.add(user_guess)

            print(f"You have already guessed '{user_guess}' letter.\n")
        
        # Run if the user guess is a letter in the selected random word
        if user_guess in selected_word_letters_list:

            #Loop for all the letters in the selected random word
            for letter in selected_word_letters_list:
                
                # Run if the letter in the selected random word is equal to the user's guess
                if letter == user_guess:                

                    # store the index of the letter which has been used right
                    index_of_letter = selected_word_letters_list.index(letter) 
                    
                    # Assign the correctly guessed letter to the correct_guessed_letters_list
                    correct_guessed_letters_list[index_of_letter] = selected_word_letters_list[index_of_letter]

                    # make the letter in the selected_word_letters_list into a dash so it doesn't repeat again
                    selected_word_letters_list[index_of_letter] = '-'

                    # add letter to already guessed letter list 
                    already_guessed_letters_set.add(user_guess) 

        if user_guess == 'exit':
            exit()

        # Run if the user guess is wrong 
        if user_guess not in selected_word_letters_list:
            print("Wrong guess! Try again!")
            already_guessed_letters_set.add(user_guess)

        print("The word: ", end="")
        print(*correct_guessed_letters_list)
        print("------------------")

    print("Congratulations! You've guess the word correctly!")

def main():
    """Main function"""

    randomly_selected_word = select_random_word()
    selected_word_letters_list = convert_str_to_list_of_words(randomly_selected_word)
    correct_guessed_letters_list = create_list_to_store_guessed_letters(selected_word_letters_list)

    play_hangman(correct_guessed_letters_list)

if __name__ == '__main__':
    main()
