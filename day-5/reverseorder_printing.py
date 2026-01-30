#print numbers in reverse order
#concept : start, stop & step along with for loop

user_input = int(input("Enter the number: "))
for i in range (user_input, 0 , -1):  #start is user_inpu, stops at 0 and decreases by 1 each time loop runs
    print(f"Reversed number is: {i}", end ="")