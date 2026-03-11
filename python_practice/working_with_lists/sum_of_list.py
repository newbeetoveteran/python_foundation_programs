# Finding the sum of numbers in a list from user input
# concept : using for loop and append to loop through and store numbers in list

sample_list = []
sum_of_digits = 0
for i in range(3):
    num = int(input("Enter number: "))
    sample_list.append(num)
    sum_of_digits += num
print(f"Sum of digits in the list is: {sum_of_digits}")
print(f"List of numbers is {sample_list}")