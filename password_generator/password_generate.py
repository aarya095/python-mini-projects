import random
import string
import validate_user_input as validate_user_input

user_choice = []
lowercause_alphabets = string.ascii_lowercase
uppercase_alphabets = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

def take_user_choice():

    print("Enter '1' to say yes, and '0' to say no.\n")

    number_of_characters = validate_user_input.take_and_validate_length_of_characters()
    include_numbers = validate_user_input.take_and_validate_input_numbers()
    include_lower_case = validate_user_input.take_and_validate_input_lower_case()
    include_upper_case = validate_user_input.take_and_validate_input_upper_case()
    include_symbols = validate_user_input.take_and_validate_input_symbols()

    if include_numbers == 0 and include_lower_case == 0 \
        and include_upper_case == 0 and include_symbols == 0:
        print("You need to at least select one option.")
        print("Please re-run the program.")

    if include_numbers == 1:
        user_choice.append(string.digits)

    if include_lower_case == 1:
        user_choice.append(string.ascii_lowercase)
        
    if include_upper_case == 1:
        user_choice.append(string.ascii_uppercase)
        
    if include_symbols == 1:
        user_choice.append(string.punctuation)
    
    user_choice_str = ''.join(user_choice)
    
    return user_choice_str, number_of_characters

def generate_password(user_choice_str, number_of_characters):
    """Generates a randomized string from the set of choices user has made."""
    password = []
    for i in range(number_of_characters):
        password.append(random.choice(user_choice_str))
    password_str = ''.join(password)
    return password_str

def run():
    """Connects all the functions and runs them all together to effectively generate the password."""
    while True:
        print("Welcome to Password Generator!\n")
        user_choice, number_of_characters = take_user_choice()
        password = generate_password(user_choice, number_of_characters)
        print(f"Password: {password}")
        return password

if __name__ == "__main__":
    run()



    
    