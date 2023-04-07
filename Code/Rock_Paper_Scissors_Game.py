import random
import colorama

# Making a function to use it in a while loop for continuous program running.


def game():

    rock = "rock"
    paper = "paper"
    scissors = "scissors"

    # Player input logic. Lowercasing any input to make it case insensitive.
    player_move = input(f"Choose Rock, Paper or Scissors: ").lower()

    if player_move == "rock":
        player_move = rock

    elif player_move == "paper":
        player_move = paper

    elif player_move == "scissors":
        player_move = scissors

    # In case of invalid input
    else:
        raise SystemExit("Invalid input. Try again.")

    # Computer element pick logic
    computer_random_number = random.randint(1,3)

    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock

    elif computer_random_number == 2:
        computer_move = paper

    elif computer_random_number == 3:
        computer_move = scissors

    # Output of computer logic
    print(f"The computer chose: {computer_move}.")

    # Game logic
    if (player_move == scissors and computer_move == paper) or (player_move == paper and computer_move == rock) \
            or (player_move == rock and computer_move == scissors):

        print(f"You win this round! 🙂")

    elif player_move == computer_move:
        print("Draw!")

    else:

        print(f"You lose this round! 🙁")


while True:
    game()
    print()
