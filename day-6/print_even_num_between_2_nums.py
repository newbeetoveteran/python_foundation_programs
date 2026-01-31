#Print all even numbers between two given numbers.
#Concept : using for loops

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number: "))


for i in range(num1, num2+1):
    if i % 2 == 0:
        print(i, end = "\t")     # end = "\t" adding tab between numbers printed