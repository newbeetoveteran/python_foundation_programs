# Counting odd numbers in a list
# Concept: using functions and loops


original_list = []
for i in range(3):
    user_input_list = int(input("Enter list numbers: "))
    original_list.append(user_input_list)
print(f"Entered numbers are: {original_list}")

def odd_count(numbers):
    odd_num_count = 0
    for i in numbers:
        if i % 2 != 0:
            odd_num_count += 1
    return odd_num_count
print(f"Count of odd numbers in {original_list} is {odd_count(original_list)}")
