# finding the largest number in a list without using max()
# concept : using for loop

num_list = [2, 10, 3, 5]
largest_num = num_list[0]     #assuming number at index 0 as largest
for digit in num_list:
    if digit > largest_num:
        largest_num = digit
print(f"Largest number is: {largest_num}")