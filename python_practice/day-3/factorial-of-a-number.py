#program to print factorial of a number
#concept: using for loop only and not importing math lib or using factorial function

user_input = int(input("Enter the number: "))
factorial = 1
for i in range(1, user_input+1):
    factorial *= i
print(factorial)
