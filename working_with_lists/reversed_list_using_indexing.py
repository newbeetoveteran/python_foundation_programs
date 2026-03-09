#reverse numbers in the list
#concept : using indexing and for loop

sample_list = [5, 8, 2, 4]
reversed_list = []
for i in range(3, -1, -1):
    reversed_list.append(sample_list[i])                       #appending reversed list with numbers in sample list at i index everytime loop runs
print(f"Reversed list of {sample_list} is {reversed_list}")