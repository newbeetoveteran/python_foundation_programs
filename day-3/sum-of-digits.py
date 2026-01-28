#python program to print sum of digits
#concept : for loop int-str-int conversion += concept & correct ibdentation of print


user_input = int(input("Enter the number: "))
sum_of_digits = 0
for digit in str(user_input):
    sum_of_digits += int(digit)
print(sum_of_digits)