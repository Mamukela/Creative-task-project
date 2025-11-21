import random

print("you will be playing rock paper scissors lizard spock, sheldon will pick randomly")

global rounds, wins, losses, ties

rounds = 1
wins = 0
losses = 0
ties = 0

items = ["rock", "paper", "scissors", "lizard", "spock"]

play = 1

def win():
    global rounds, wins
    print("you win!")
    wins += 1
    rounds += 1 

def lose():
    global rounds, losses
    print("you lose!")
    losses += 1
    rounds += 1 

def tie():
    global rounds, ties
    print("its a tie!")
    ties += 1
    rounds += 1 

while True:
    print("round ", rounds)
    selection = random.choice(items)
    print("make your selection, or type end to stop the game.")
    choice = input()
    if choice == "end":
        break

    print("you chose ", choice, ", sheldon chose ", selection)
    
    match (choice, selection):
        case (c, s) if c == s:
            tie()
        # rock
        case ("rock", "paper"):
            print("paper covers rock,")
            lose()
        case ("rock", "scissors"):
            print("rock crushes scissors,")
            win()
        case ("rock", "lizard"):
            print("rock crushes lizard,")
            win()
        case ("rock", "spock"):
            print("spock vaporizes rock,")
            lose()
        # paper
        case ("paper", "rock"):
            print("paper covers rock,")
            win()
        case ("paper", "scissors"):
            print("scissors cut paper,")
            lose()
        case ("paper", "lizard"):
            print("lizard eats paper,")
            lose()
        case ("paper", "spock"):
            print("paper disproves spock,")
            win()
        # scissors
        case ("scissors", "rock"):
            print("rock crushes scissors,")
            lose()
        case ("scissors", "paper"):
            print("scissors cut paper,")
            win()
        case ("scissors", "lizard"):
            print("scissors decapitate lizard,")
            win()
        case ("scissors", "spock"):
            print("spock crushes scissors,")
            lose()
        # lizard
        case ("lizard", "rock"):
            print("rock crushes lizard,")
            lose()
        case ("lizard", "paper"):
            print("lizard eats paper,")
            win()
        case ("lizard", "scissors"):
            print("scissors decapitate lizard,")
            lose()
        case ("lizard", "spock"):
            print("lizard poisons spock,")
            win()
        # spock
        case ("spock", "rock"):
            print("spock vaporizes rock,")
            win()
        case ("spock", "paper"):
            print("paper disproves spock,")
            lose()
        case ("spock", "scissors"):
            print("spock crushes scissors,")
            win()
        case ("spock", "lizard"):
            print("lizard poisons spock,")
            lose()
        case _:
            print("invalid selection, please choose from:", ", ".join(items))



print("game end, stats:")

print("rounds played: ", rounds - 1)
print("wins: ", wins)
print("losses: ", losses)
print("ties: ", ties)

