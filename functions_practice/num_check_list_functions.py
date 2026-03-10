# Finding if a number exists in the list
# Concept : Using list and loop.

static_list = []
for i in range(3):
    user_input_list = int(input(f"Enter the number in the list {i+1}: "))
    static_list.append(user_input_list)
print(f"User inputs are: {static_list}")

def contains_num(numbers, target_num):
    num_check = False
    for i in numbers:
        if i == target_num:
            return True
    return False
target_num = int(input("Enter number you want to search: "))
print(f"{target_num} exists in your list? {contains_num(static_list, target_num)}.")