# Remove duplicate numbers from the list
# Concept : function, list and loop

original_list = []

for i in range(5):
    user_input = int(input(f"Enter elements of the list {i+1}: "))
    original_list.append(user_input)
print(f"Entered list elements are: {original_list}")

def duplicate_num_check(numbers):
    num_checked = []
    duplicate_num = []
    for num in numbers:

        if num in num_checked and num not in duplicate_num:
            duplicate_num.append(num)
        else:
            num_checked.append(num)
    return num_checked, duplicate_num

seen, duplicate = duplicate_num_check(original_list)

print(f"Duplicate elements in {original_list} are: {duplicate}")
print(f"List without duplicate elements in {original_list} is: {seen}")