#ROCK PAPER SCISSOR

import random

def game(computer,player):
    if computer==player:
        return None
    elif computer == 'Rock':
        if player == 'Paper':
            return True
        elif player == 'Scissor':
            return False
    elif computer == 'Paper':
        if player == 'Scissor':
            return True
        elif player == 'Rock':
            return False
    elif computer == 'Scissor':
        if player == 'Paper':
            return True
        elif player == 'Rock':
            return False
    
print("Computer Turn: Rock(R) Paper(P) or Scissor(S)")
randNo = random.randint(1,3)
if randNo == 1:
    computer = "Rock"
if randNo == 2:
    computer = "Paper"
if randNo == 3:
    computer = "Scissor"

player = input("Your Turn: Rock(R) Paper(P) or Scissor(S)\n")
a = game(computer,player)

print(f"Computer chose: {computer}")
print(f"Computer chose: {player}")

if a==None:
    print("Game is a Tie!")
elif a:
    print("You Lose!")
else:
    print("You Win!")
