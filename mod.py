import random

print("you will be playing rock paper scissors lizard spock, sheldon will pick randomly")

rounds = 1
win = 0
loss = 0
tie = 0

items = ["rock", "paper", "scissors", "lizard", "spock"]

play = 1

while True:
    print("round ", rounds)
    selection = random.choice(items)
    print("make your selection, or type end to stop the game.")
    choice = input()
    if choice == "end":
        break
    print("you chose ", choice, ", sheldon chose ", selection)
    
    if choice == selection:
        print("it's a tie")
        tie += 1
    #rock
    elif choice == "rock" and selection == "paper":
        print("paper covers rock, you lose.")
        loss += 1
    elif choice == "rock" and selection == "scissor":
        print("rock crushes scissor, you win.")
        win += 1
    elif choice == "rock" and selection == "lizard":
        print("rock crushes lizard, you win.")
        win += 1
    elif choice == "rock" and selection == "spock":
        print("spock vaporizes rock, you lose.")
        loss += 1
    #paper
    elif choice == "paper" and selection == "rock":
        print("paper covers rock, you win.")
        win += 1
    elif choice == "paper" and selection == "scissors":
        print("scissors cut paper, you lose.")
        loss += 1
    elif choice == "paper" and selection == "lizard":
        print("lizard eats paper, you lose.")
        loss += 1
    elif choice == "paper" and selection == "spock":
        print("paper disproves spock, you win.")
        win += 1
    #scissor
    elif choice == "scissors" and selection == "rock":
        print("rock crushes scissors, you lose.")
        loss += 1
    elif choice == "scissors" and selection == "paper":
        print("scissors cut paper, you win.")
        win += 1
    elif choice == "scissors" and selection == "lizard":
        print("scissors decapitate lizard, you win.")
        win += 1
    elif choice == "scissors" and selection == "spock":
        print("spock crushes scissors, you lose.")
        loss += 1
    #lizard
    elif choice == "lizard" and selection == "rock":
        print("rock crushes lizard, you lose")
        loss += 1
    elif choice == "lizard" and selection == "paper":
        print("lizard eats paper, you win")
        win += 1
    elif choice == "lizard" and selection == "scissors":
        print("scissors decapitate lizard, you lose.")
        loss += 1
    elif choice == "lizard" and selection == "spock":
        print("lizard poisons spock, you win")
        win += 1
    #spock
    elif choice == "spock" and selection == "rock":
        print("spock vaporizes rock, you win")
        win += 1
    elif choice == "spock" and selection == "paper":
        print("paper disproves spock, you lose")
        loss += 1
    elif choice == "spock" and selection == "scissors":
        print("spock crushes scissors, you win")
        win += 1
    elif choice == "spock" and selection == "lizard":
        print("lizard posions spock, you lose")
        loss += 1
    rounds += 1

print("game end, stats:")

print("rounds played: ", rounds)
print("wins: ", win)
print("losses: ", loss)
print("ties: ", tie)

