# sum of numbers in a list
# Concept: using functions and user input

original_list = []
for i in range(5):
    user_entered_list = int(input("Enter the numbers: "))
    original_list.append(user_entered_list)
print(f"Entered numbers are: {original_list}")

def sum_list(numbers):
    num_sum = 0
    for i in numbers:
        num_sum += i
    return num_sum
print(f"Sum of numbers in the list is: {sum_list(original_list)}")