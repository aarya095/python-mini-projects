import string

number_of_characters = 8
include_numbers = -1
include_lower_case = -1
include_upper_case = -1
include_symbols = -1
validation_list_of_1_or_0 = [1,0]

def take_and_validate_input_password():
    """Takes in and validates the user's password on set of conditions"""
    lowercase_alphabets = string.ascii_lowercase
    uppercase_alphabets = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation
    track_passwd_parameters = set()
    
    while True:

        input_password = input("Enter password: ")

        for character in input_password:
            if character in numbers:
                track_passwd_parameters.add('a')
            if character in lowercase_alphabets:
                track_passwd_parameters.add('b')
            if character in uppercase_alphabets:
                track_passwd_parameters.add('c')
            if character in symbols:
                track_passwd_parameters.add('d')

        if len(track_passwd_parameters) < 4:
            track_passwd_parameters = set()
            print("The password should contain at least one symbol, uppercase, lowercase, and number.")
        elif len(input_password) < 8:
            print("The password should contain at least 8 characters.")
        elif (len(track_passwd_parameters) == 4 and len(input_password) > 8):
            break
    return input_password

def take_and_validate_length_of_characters():
    """Takes in length_of_character and validates it, loops until the user provides the accepted input"""
    
    while True:
        try:
            number_of_characters = int(input("Length of Password: "))            
            if 8 < number_of_characters < 32:
                break
            if number_of_characters < 8 or number_of_characters > 32:
                print("Please input password length atleast 8 characters and atmost 32 characters.")

        except ValueError:
            print("Invalid Input! Please provide an integer.")

    return number_of_characters



def take_and_validate_input_numbers():
    """Takes in length_of_character and validates it, loops until the user provides the accepted input"""
    
    while True:
        try:
            include_numbers = int(input("Do you want to include numbers: "))
            if include_numbers in validation_list_of_1_or_0:
                break
            if include_numbers not in validation_list_of_1_or_0:
                print("Please input either 1 or 0.")

        except ValueError:
            print("Invalid Input! Please provide an integer.")

    return include_numbers

def take_and_validate_input_lower_case():
    """Takes in length_of_character and validates it, loops until the user provides the accepted input"""
    
    while True:
        try:
            include_lower_case = int(input("Do you want to include lower case characters: "))
            if include_lower_case in validation_list_of_1_or_0:
                break
            if include_lower_case not in validation_list_of_1_or_0:
                print("Please input either 1 or 0.")

        except ValueError:
            print("Invalid Input! Please provide an integer.")

    return include_lower_case

def take_and_validate_input_upper_case():
    """Takes in length_of_character and validates it, loops until the user provides the accepted input"""
    
    while True:
        try:
            include_upper_case = int(input("Do you want to include upper case characters: "))
            if include_upper_case in validation_list_of_1_or_0:
                break
            if include_upper_case not in validation_list_of_1_or_0:
                print("Please input either 1 or 0.")

        except ValueError:
            print("Invalid Input! Please provide an integer.")

    return include_upper_case

def take_and_validate_input_symbols():
    """Takes in length_of_character and validates it, loops until the user provides the accepted input"""
    
    while True:
        try:
            include_symbols = int(input("Do you want to include symbols: "))
            if include_symbols in validation_list_of_1_or_0:
                break
            if include_symbols not in validation_list_of_1_or_0:
                print("Please input either 1 or 0.")

        except ValueError:
            print("Invalid Input! Please provide an integer.")

    return include_symbols

if __name__ == '__main__':
    take_and_validate_input_password()