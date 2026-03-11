# This program prints a sequence of numbers in reverse order, starting from 10 down to 1.
# concept: for loop, range function, end parameter in print function

num_range = 10
count = 0
row_count = 4
for num in range (num_range, 0, -1):
    print(num, end=' ')
    count += 1
    if count == row_count:
        print()
        row_count -= 1
        count = 0