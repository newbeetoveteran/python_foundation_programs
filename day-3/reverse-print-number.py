#program to print the digits of a number in reverse order
#concepts: loops, string manipulation, user input

user_input = input("Enter the number: ")
for digit in (user_input) [::-1]:
    print(digit, end="")

# Alternative version converting digits back to int

user_input = int(input("Enter the number: "))
for digit in str(user_input) [::-1]:
    print(int(digit), end="")