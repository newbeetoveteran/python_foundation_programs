#adding numbers starting from 1 until total becomes > 100
#using while loop concept

input_num = int(input("Enter a positive number less than 100: "))

total = 0

i = 1
while i <= input_num:
    total += i
    if total > 100:
        print("Total value has reached 100. Exiting code!")
        break
    i += 1
print(f"Total sum: {total}")
