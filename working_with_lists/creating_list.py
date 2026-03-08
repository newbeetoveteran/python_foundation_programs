#creating a list by taking user input
#using for loop and range function

numbers = []

for i in range(5):
    num = int(input("Enter numbers: "))
    numbers.append(num)

print(numbers)