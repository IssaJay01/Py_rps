import random

game_over = 10;
player_score = 0;
cpu_score = 0;

print("Lets play rock, paper, scissors! First to 10 wins is the winner.")
player_name = input("My name is Ordiz, what is your name? ")

while cpu_score < game_over and player_score < game_over:

    player_input = input(f"\nOk {player_name}, Enter rock, paper, or scissors: ")

    if player_input not in ["rock", "paper", "scissors"]:
        print("\nDude! You didn't follow instructions and im sorry but you're disqualified.")
        quit()
    else:
        cpu_options = ["rock", "paper", "scissors"]
        cpu_input = random.choice(cpu_options)
        print(f"You chose {player_input} and I chose {cpu_input}.\n")

        if player_input == cpu_input:
            print(f"We both selected {player_input}! Ugh, we tied...")
            print(f"The score is {player_name}:{player_score} - Ordiz:{cpu_score}")

        # If player chooses rock...
        elif player_input == "rock":
            if cpu_input == "scissors":
                print("Rock breaks scissors. You win this round I guess.")
                player_score += 1
                print(f"The score is {player_name}:{player_score} - Ordiz:{cpu_score}")
            else:
                print("Paper covers rock! You lose!")
                cpu_score += 1
                print(f"The score is {player_name}:{player_score} - Ordiz:{cpu_score}")

        # If player chooses paper...
        elif player_input == "paper":
            if cpu_input == "rock":
                print("Paper covers rock. You win this round. Don't get cocky.")
                player_score += 1
                print(f"The score is {player_name}:{player_score} - Ordiz:{cpu_score}")
            else:
                print("Scissors cuts paper! You lose! Loser!")
                cpu_score += 1
                print(f"The score is {player_name}:{player_score} - Ordiz:{cpu_score}")

        # If player chooses scissors...
        elif player_input == "scissors":
            if cpu_input == "paper":
                print("Scissors cuts paper. Whatever, you win this round.")
                player_score += 1
                print(f"The score is {player_name}:{player_score} - Ordiz:{cpu_score}")
            else:
                print("Rock breaks scissors! You lose! You suck!")
                cpu_score += 1
                print(f"The score is {player_name}:{player_score} - Ordiz:{cpu_score}")

if player_score == 10:
    print(f"\nCongrats to you {player_name} for beating me with a score of {player_score} to {cpu_score}.")
    print("You won't win next time!")
    quit()
elif cpu_score == 10:
    print(f"\nSorry {player_name} but I win this time with a score of {cpu_score} to {player_score}!")
    print("Better luck next time!")
    quit()


