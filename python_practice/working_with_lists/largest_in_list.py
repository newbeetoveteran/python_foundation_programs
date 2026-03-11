#find the largest number in the list

input_list = [5, 8, 2, 9, 1]
largest_num = input_list[0]
for i in input_list:
    if i > largest_num:
        largest_num = i
print(f"Largest number in {input_list} is {largest_num}")
