import random
user_score = 0
computer_score = 0
while True:
    options = ["Rock", "Paper", "Scissor"]
    while True:
        user_input = int(input("Enter 1 for Rock,2 for Paper,3 for Scissor: "))
        if user_input == 1 or user_input == 2 or user_input == 3:
            break
        else:
            print("Invalid Input")
    user_choice = options[user_input - 1]
    print("User's choice: ", user_choice)
    computer_choice = random.choice(options)
    print("Computer's choice: ", computer_choice)
    if user_choice == computer_choice:
        print("Round tied")
    elif user_choice == "Rock":
        if computer_choice == "Scissor":
            print("User wins round")
            user_score += 1
        else:
            print("Computer wins round")
            computer_score += 1
    elif user_choice == "Paper":
        if computer_choice == "Rock":
            print("User wins round")
            user_score += 1
        else:
            print("Computer wins round")
            computer_score += 1
    else:
        if computer_choice == "Paper":
            print("User wins round")
            user_score += 1
        else:
            print("Computer wins round")
            computer_score += 1
    print("User score: ", user_score)
    print("Computer score", computer_score)
    while True:
        repeat = int(input("Enter 0 to end game, 1 to play again: "))
        if repeat == 0 or repeat == 1:
            break
        else:
            print("Invalid Input")
    if repeat == 0:
        print("Game ended")
        print("User score: ", user_score)
        print("Computer score", computer_score)
        if user_score == computer_score:
            print("Game tied")
        elif user_score > computer_score:
            print("User wins game")
        else:
            print("Computer wins game")
        break
