#count digits - program to count the number of digits in a number
#concept : using while loop, reversing number, floor division and no string conversion

user_input = int(input("Enter the number (greater than 0): "))
original_user_input = user_input
digit_count = 0
while user_input > 0:
    digit = user_input % 10
    digit_count += 1
    user_input = user_input // 10
print(f"Number of digits in {original_user_input} is {digit_count}")