# check if a number is Palindrome
# concept : using while loop to check Palindrome

user_input = int(input("Enter the number(except negative numbers): "))
original_num = user_input
reverse = 0
while user_input > 0:
    digit = user_input % 10
    reverse = reverse * 10 + digit
    user_input = user_input // 10
if reverse == original_num:
    print("This number is Palindrome")
else:
    print("This number is not a Palindrome")
    
