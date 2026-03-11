# Program to double every number in the list
# Concept: Using functions, list and for loop

original_list = []
for i in range (4):
    user_input_list = int(input(f"Enter the number in list {i+1}: "))
    original_list.append(user_input_list)
print(f"Entered list numbers are: {original_list}")

def double_list(numbers):
    doubled = []
    for i in numbers:
        doubled.append(i*2)
    return doubled
print(f"Double of the list {original_list} is {double_list(original_list)}")