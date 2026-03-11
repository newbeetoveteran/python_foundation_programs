
#python program to print centre aligned pyramid
#concept : use input from user and use for loops to iterate spaces and stars

user_input = int(input("Enter the size of pyramid: "))
spaces = " "
stars = "*"
for i in range(1, user_input+1):
    if user_input >0:
        print(spaces * (user_input - i) + stars * (2 * i - 1))

else:
    print("Invalid input! Please enter number greater than 0.")