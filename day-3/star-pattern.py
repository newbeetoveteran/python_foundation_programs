#progra, to print a simple star pattern
#concept : using for loop

user_input = int(input("Enter the size of star pattern between 5 to 10: "))
count = 0
for i in range(0, user_input+1):
    print("*"*i)