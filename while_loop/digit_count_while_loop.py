# Python program to ask the user for a number and count how many digits it has
# forcing while loop

user_input = input("Enter the number to check: ")
digit_count = 0
while digit_count<len(user_input):
    print(user_input[digit_count])
    digit_count += 1
print(f"Total digits in {user_input} is : {len(user_input)}")