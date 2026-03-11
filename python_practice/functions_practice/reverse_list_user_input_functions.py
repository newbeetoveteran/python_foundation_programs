# Reversing number from user input list
# Concept: for loop, append, reverse indexing

list_nums = []
for i in range(4):
    user_input = int(input("Enter the number: "))
    list_nums.append(user_input)
print(f"Entered list is: {list_nums}")

def reversed_list(numbers):
    reversed_num = []
    for i in range(len(numbers)- 1, -1, -1):
        reversed_num.append(numbers[i])
    return reversed_num
print(f"Reversed list is {reversed_list(list_nums)}")