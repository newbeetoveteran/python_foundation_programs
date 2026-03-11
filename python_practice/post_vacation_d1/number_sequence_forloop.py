# Program to print the number sequence in a triangular pattern
# Concept : Using for loop once

num_range = 10 
count = 0         # to keep track of the number of elements printed in the current row
row_count = 1                                  # to keep track of the number of rows printed, starting with row 1
for num in range(1, num_range + 1):
    print(num, end=' ')
    count += 1                               # Increment the count of numbers printed in current row

    if count == row_count:
        print()                              # move to next line after printing required numbers in current row
        row_count += 1                       # Increment row count for next row
        count = 0                            # Reset count for the next row