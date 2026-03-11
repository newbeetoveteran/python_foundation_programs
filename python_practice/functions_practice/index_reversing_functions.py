#Program to reverse numbers in the list
#Concept : using functions, reverse indexing for loop

sample_list = [9, 2, 6, 5]

def reversed_list(numbers):
    reversed_num = []
    for i in range(len(numbers) - 1, -1, -1):
        reversed_num.append(numbers[i])
    return reversed_num
print(f"Reversed list is: {reversed_list(sample_list)}")