# Find the largest number in the list
# Concept : Using function, loops and append. Not using the max function

main_list = []

for i in range(4):
    user_input = int(input(f"Enter the list item number {i+1}: "))
    main_list.append(user_input)
print(f"Entered list is {main_list}")

def max_num(numbers):
    largest = numbers[0]
    for i in numbers:
        if i > largest:
            largest = i
    return largest
print(f"Largest number in {main_list} is {max_num(main_list)}")