# program to reverse the number using functions
# concept : functions, returning function reversing using insert

sample_list = [5, 8, 2, 4]
def reverse_list(numbers):
    reversed_num = []
    for i in numbers:
        reversed_num.insert(0,i)
    return reversed_num
print(f"Reversed list is: {reverse_list(sample_list)}")