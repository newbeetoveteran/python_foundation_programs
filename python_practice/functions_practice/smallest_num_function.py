#finding smallest number in the list
#Concept : Using function to define the operation and for loop

original_list = []
for i in range (3):
    user_input = int(input("Enter the number: "))
    original_list.append(user_input)
print(f"Entered list number is: {original_list}")

def find_min(numbers):
    smallest_num = numbers[0]
    for i in numbers:
        if i <= smallest_num:
            smallest_num = i
    return smallest_num
print(f"Smallest number in list is: {find_min(original_list)}")