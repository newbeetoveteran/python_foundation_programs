#pythom program to check if a number is a palindrome
#concept : using simple if else


user_input = input("Enter the number to check Palindrome: ")
if user_input == user_input[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome.")