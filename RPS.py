import random
myList = ['rock','paper','scissors']

class Game:
    def play(playerSelection):
        computerSelection = random.choice(myList)
        if (playerSelection == 'rock' and computerSelection == 'rock'):
            print(f'You chose {playerSelection} and the Computer chose {computerSelection}. Tie')
        elif (playerSelection == 'rock' and computerSelection =='paper'):
            print(f'You chose {playerSelection} and the Computer chose {computerSelection}. You Lose')
        elif (playerSelection == 'rock' and computerSelection == 'scissors'):
            print(f'You chose {playerSelection} and the Computer chose {computerSelection}. You Win')

Game.play('rock')