# menu-based-py program
# concept : using if-elif-else for menu selection

print("Please select from the following options")
print("1. Pizza ")
print("2. Burger")

user_selection = input("Enter the menu number: ")
if user_selection == '1':
    print("Your order for Pizza has been placed.")
elif user_selection == '2':
    print("Your order for Burger has been placed.")
else:
    print("Invalid selection. Please choose either 1 or 2.")