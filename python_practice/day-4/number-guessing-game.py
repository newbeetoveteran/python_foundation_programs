#python program to guess the number
#concept : if-elif statement

player_name = input("Enter your name: ")
print(f"Hi {player_name}! Let's play a number guessing game. I am thinking of a number. You have to guess that number.")

player_input_num = int(input("Enter number between 1 to 5: "))
num = 3

if player_input_num == num:
    print(f"Congratulations {player_name}! You guessed the correct number. 🥳")
elif player_input_num > num and player_input_num < 5:
    print("Entered number is high. You've lost!! 🤪")
elif player_input_num < num and player_input_num != 0:
    print("Entered number is low. You've lost!! 😒")
elif player_input_num > 5:
    print("Entered number is not valid input. Please enter number between 1 & 5!")