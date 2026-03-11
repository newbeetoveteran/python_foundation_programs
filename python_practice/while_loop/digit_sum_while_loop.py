#python program to find sum of digits from user input
#using while loop

user_input = int(input("Enter the number: "))

digit_sum = 0

while user_input > 0 :
    digit = user_input % 10             # % 10 Gives last digit in the number, which is stored in digit var
    digit_sum += digit                  # updating the digit_sum value everytime while loop runs with last value 
    user_input = user_input // 10       # // 10 removes the last digit from the number leaving new num excluding last digit
print(digit_sum)