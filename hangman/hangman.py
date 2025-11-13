# Hangman game
"""
computer will select a word from a predefined list of words. 
"""

from words import words
import random

correct_guessed_letters_list = []
already_guessed_letters_set = set() # consists of both correct guesses and incorrect guesses
selected_word_letters_list = []

def select_random_word():
    x = random.choice(words)
    return x 

def convert_str_to_list_of_words(randomly_selected_word):
    print(randomly_selected_word)

    for letter in randomly_selected_word:
        selected_word_letters_list.append(letter)
    print(selected_word_letters_list)
    return selected_word_letters_list

def create_list_toStore_guessed_letters(selected_word_letters_list):
    for i in range(0,len(selected_word_letters_list)):
        correct_guessed_letters_list.append('-')
    print(correct_guessed_letters_list)
    return correct_guessed_letters_list

def play_hangman(correct_guessed_letters_list):
    while selected_word_letters_list != correct_guessed_letters_list:
        user_guess = input("Please guess a letter: ").strip().lower()
        if len(already_guessed_letters_set) != 0:
            print(f"\nAlready used letters: {already_guessed_letters_set}")

        if user_guess in correct_guessed_letters_list or user_guess in already_guessed_letters_set:
            already_guessed_letters_set.add(user_guess)
            print(f"You have already guessed '{user_guess}' letter")
        
        elif user_guess in selected_word_letters_list:
            print(selected_word_letters_list)
            index_of_letter = selected_word_letters_list.index(user_guess)
            print(index_of_letter)
            correct_guessed_letters_list[index_of_letter] = selected_word_letters_list[index_of_letter]
            print(f"The word: {correct_guessed_letters_list}")
            already_guessed_letters_set.add(user_guess)

        elif user_guess == 'exit':
            exit()

        elif user_guess not in selected_word_letters_list:
            print("Wrong guess! Try again!")
            already_guessed_letters_set.add(user_guess)

    print("\nCongratulations! You've guess the word correctly!")

def run():
    randomly_selected_word = select_random_word()
    selected_word_letters_list = convert_str_to_list_of_words(randomly_selected_word)
    correct_guessed_letters_list = create_list_toStore_guessed_letters(selected_word_letters_list)
    play_hangman(correct_guessed_letters_list)

run()
