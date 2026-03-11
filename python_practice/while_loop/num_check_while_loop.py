#checking if number 7 exists in the 
# Concept : using while loop, break and floor division

user_input_num = int(input("Enter the number to check : "))
num_check = False
while user_input_num > 0:
    digit = user_input_num % 10
    if digit == 7:
        num_check = True
        break
    user_input_num = user_input_num // 10
if num_check == True:
    print("7 Exists.")
else:
    print("Not found!")