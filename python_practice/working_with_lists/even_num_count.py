#even number count in a list

sample_list = [2, 5, 8, 7, 10]
count = 0
for i in sample_list:
    if i % 2 == 0:
        count += 1
print(f"Total number of even numbers in {sample_list} is {count}")