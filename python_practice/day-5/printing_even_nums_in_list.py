# python program to check all even numbers in the list of user input range
# concept: using for loop
# Note: there is a flaw in this code that the else condition is only true for 0


user_input_list = int(input("Enter the list range: "))

for i in range(user_input_list+1):
    if i % 2 == 0:
       print(i)
else:
    print("List contains odd numbers only")