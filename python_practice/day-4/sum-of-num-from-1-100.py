#python program to print the sum of numbers from 1 to 100 using a for loop.

user_input = int(input("Enter the number between 1 - 100: "))
sum_of_numbers = 0
for i in range(1, user_input+1):
    sum_of_numbers += i
print(f"sum of num: {sum_of_numbers}")