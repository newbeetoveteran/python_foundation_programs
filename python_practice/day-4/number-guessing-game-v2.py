
player_name = input("Who's playing? ")
print(f"Hi {player_name}! I am thinking a number & you've to guess the number...")
player_input = int(input("Enter the number: "))
game_number = 4

if player_input < 0:
    print(f"Negative numbers are not allowed. Try again {player_name}")
elif player_input == 0:
    print("Please select number other than 0.")

elif player_input == game_number:
    print(f"You've guessed the correct number! Congratulations {player_name}")

elif player_input > game_number:
    print(f"You've guessed number higher than what I am thinking {player_name}. You lost")

elif player_input < game_number:
    print(f"You've guessed number lower than what I am thinking {player_name}. You lost")

else:
    print("Invalid input")