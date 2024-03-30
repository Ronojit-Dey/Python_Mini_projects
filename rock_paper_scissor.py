import random

def play():
    user = input("What's your choice? Enter r for rock, p for paper, or s for scissors: ")
    computer = random.choice(["r", 'p', 's'])

    if user == computer:
        return "It's a tie!"
    
    # r beats s, s beats p, p beats r 
    if isWin(user, computer):
        return "You WON!"

    return "You lost!"

def isWin(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    else:
        return False

while True:  
    print(play())
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        break 