# reversing a number

user_input = int(input("Enter the number to be reversed: "))
original_user_input = user_input
reverse_num = 0
while user_input > 0:
    digit = user_input % 10
    reverse_num = reverse_num * 10 + digit
    user_input = user_input // 10
print(f"Reverse of the number {original_user_input} is {reverse_num}")