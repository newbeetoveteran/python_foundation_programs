# printing numbers from 1 to n
# concept : using for loop and range function along with end parameter in print function to print in same line
# end parameter sets default print end with space instead of new line

user_input = int(input("Enter the number: "))

for i in range(user_input):
    print(i+1, end = " ")        