import random

# User Input
user_input = input("(R)ock, (P)aper, (S)cissors? ").lower()

# Computer Random Choice
ai_random = random.randint(1, 3)

# variables to hold the words
user_word = ""
ai_word = ""

# Map User Input to Word
if user_input == 'r':
    user_word = "Rock"
elif user_input == 'p':
    user_word = "Paper"
elif user_input == 's':
    user_word = "Scissors"

# Check for invalid input BEFORE continuing
if user_word == "":
    print("Bad choice...")
else:
    # Map Computer Number to Word
    if ai_random == 1:
        ai_word = "Rock"
    elif ai_random == 2:
        ai_word = "Paper"
    elif ai_random == 3:
        ai_word = "Scissors"

    #  Display Choices
    print(f"Player choice : {user_word}")
    print(f"Computer choice : {ai_word}")

    #  Determine Winner
    if user_word == ai_word:
        print("Tie !")
    
    # Winning conditions for the Player
    elif (user_word == "Rock" and ai_word == "Scissors") or \
         (user_word == "Scissors" and ai_word == "Paper") or \
         (user_word == "Paper" and ai_word == "Rock"):
        print("The winner is the player")
    
    else:
        # If it's not a tie and the player didn't win, the computer wins
        print("The winner is the computer")