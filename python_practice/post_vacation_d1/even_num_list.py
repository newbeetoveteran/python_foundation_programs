#python program to print even numbers in a list, count the even numbers in the list and print sum of the even numbers
#concept : using count and for loop concept

num_list = [4,7,2,9,12,15]
even_num = []
count = 0
for i in num_list:
    if i % 2 == 0:
        count += 1
        even_num.append(i)
print(f"Even num list is: {even_num}")
print(f"Count of even numbers: {count}")
print(f"Sum of even nums: {sum(even_num)}")