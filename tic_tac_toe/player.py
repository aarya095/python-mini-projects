import random

def assign_x_or_o_to_player():
    """Assigns X or O randomly to either player"""

    human_player = None
    computer_player = None
    x_or_o_choice = ['X','O']

    human_player = random.choice(x_or_o_choice)
    if human_player == 'X':
        computer_player = 'O'
    else:
        computer_player = 'X'

    players_dict = {
        'human_player' : human_player,
        'computer_player' : computer_player
    }

    return players_dict

if __name__ == '__main__':
    #human_player, computer_player = assign_x_or_o_to_player()
    #print(human_player, computer_player)
    mylist = [1,2,3,4,5,6]
    myStr = str(mylist)
    print(myStr)