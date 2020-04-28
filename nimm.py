"""
File: nimm.py
-------------------------
Python version of the nimm game. There are 20 stones and 2 players. Each player decides to remove
1 or 2 stones in their turn. The last player to remove a stone loses.

You can also play against AI in this game but the AI will always win.
"""

def main():
    ai = check_play_against_ai()
    stones_left = 20
    player = 1

    while stones_left > 0:
        print("\nThere are " + str(stones_left) + " stones left")
        if player == 2 or not ai:
            stones_left -= get_stones_to_remove(player)
        else:
            stones_left -= ai_turn(stones_left)
        player = update_player_number(player)
    print("\n\nPlayer " + str(player) + " wins!!")


# Prompt the player to choose between playing against AI or against another player.
# Returns true if the player plays against the AI and false if the player plays against another player
def check_play_against_ai():
    print("1) Play against AI")
    print("2) Play against another player")
    user_option = int(input("\nChoose option 1 or 2: "))

    if user_option == 1:
        print("\nAI is Player 1")
        return True
    return False

# Ask the player how many stones to remove.
# Checks if the input is not correct. In that case, will ask the player until it is correct.
def get_stones_to_remove(player):
    stones_to_remove = int(input("Player " + str(player) + " would you like to remove 1 or 2 stones? "))
    while stones_to_remove != 1 and stones_to_remove != 2:
        stones_to_remove = int(input("Please enter 1 or 2: "))
    return stones_to_remove

 
# If the player decided to play against the AI, this will be called in AIs turn
# AI will remove 1 stone in the first turn of the game
# After the first turn, AI will 2 stones if the player removes 1 and 1 stone if the player removes 2
# Removing 3 stones always in each turn, so the player will be the last to remove
# If the stones left modulus 3 returns 0, it means the AI will have to remove 2 stones.
# Start of the turn: 16 stones
# Player removes 1
# 15 stones left, modulus 3 returns 0, then AI removes 2
# If Player removes 2
# 14 stones left, modulus 3 does not return 0 so AI removes 1 stone.
def ai_turn(stones_left):
    if stones_left % 3 == 0:
        print("AI removes 2 stones")
        return 2
    else:
        print("AI removes 1 stone")
        return 1
        
# Changes player number after each turn
def update_player_number(player_n):
    if player_n == 1:
        return 2
    else:
        return 1


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
