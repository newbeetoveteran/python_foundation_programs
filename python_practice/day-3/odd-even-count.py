#python program to count odd and even numbers from 0 to n
#concepts: loops, conditionals, user input

user_input = int(input("Enter the number: "))
even_count = 0
odd_count = 0

#using user_input+1 to include user_input in the range

for i in range(0, user_input+1):
    if i%2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Total odd numbers between 0 and {user_input} is: {odd_count}")
print(f"Total even numbers between 0 and {user_input} is: {even_count}")