# program to get the product of digits in user input
# concept : using while loop

user_input = int(input("Enter the numbr: "))
num_product = 1

while user_input> 0:
    digit = user_input % 10
    num_product *= digit
    user_input = user_input//10
print(f"Product of digits is {num_product}")