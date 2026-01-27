# Python program to print the table of a given number
# concpts: loops, user input


user_input = int(input("Enter the number: "))
for i in range(1, 11):                                 
    
     # using range to iterate from 1 to 10 
     # so that program does not run infinitely or only for range of user input

    print(f"{user_input} x {i} = {user_input * i}")