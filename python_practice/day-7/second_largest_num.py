# Python program to find the second largest number in the list
# Concept : usage of for loop and list

num_list = [1,4,5,8]
largest = num_list[0]
second_largest = num_list[0]

for digit in num_list:
    if digit > largest:
        second_largest = largest
        largest = digit
    elif digit > second_largest and digit != largest:
        second_largest = digit
print(f"The largest number is : {largest}")
print(f"The second largest number is : {second_largest}")