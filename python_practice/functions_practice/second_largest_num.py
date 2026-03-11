# Code to find the second largest number in the list
# Concept: using function and user input along with loop

static_list = []

for i in range(4):
    user_input_list = int(input(f"Enter the list item(non-negative) {i+1}: "))
    static_list.append(user_input_list)
print(f"User entered: {static_list}")

def second_largest_num(numbers):
    largest_num = numbers[0]
    second_largest = numbers[1]

    if second_largest > largest_num:
        largest_num, second_largest = second_largest, largest_num
    
    for i in numbers:
        if i > largest_num:
            second_largest = largest_num
            largest_num = i
        elif i > second_largest:
            second_largest = i
    return second_largest

print(f"Second largest in user entered list is : {second_largest_num(static_list)}")