# finding the largest digit in the user_input
# concept: while loop and reverse of the number

user_input = int(input("Enter the number(non negative): "))
original_num = user_input
largest_digit = 0
while user_input > 0:
    digit = user_input % 10
    if digit > largest_digit:
        largest_digit = digit
    user_input = user_input // 10
print(f"Largetst digit in {original_num} is {largest_digit}")