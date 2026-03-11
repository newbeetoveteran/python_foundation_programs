# finding smalllest number in a list

sample_list = [7, 2, 9, 4, 1]
smallest_num = sample_list[0]
for i in sample_list:
    if i < smallest_num:
        smallest_num = i
print(f"Smallest number in {sample_list} is {smallest_num}")