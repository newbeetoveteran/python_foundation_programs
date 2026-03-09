#reverse the numbers in list
# concept : using insert

sample_list = [3, 7, 1]
reversed_list = []

for i in sample_list:
    reversed_list.insert(0,i)
print(reversed_list)