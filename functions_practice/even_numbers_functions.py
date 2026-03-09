# Program to find even numbers in a list
# Concept : loops, functions and append

original_list = []
for i in range(4):
    user_input = int(input("Enter the number: "))
    original_list.append(user_input)
print(f"Entered list is: {original_list}")

def even_num(numbers):
    list_items = []
    for i in numbers:
        if i % 2 == 0:
            list_items.append(i)
    return list_items
print(f"Even number/s in the list are: {even_num(original_list)} ")