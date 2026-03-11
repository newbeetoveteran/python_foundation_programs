#python program to calculate discount on items over a certain price
#concept - if else statements to check item price and apply discount

user_input = int(input("Enter the cost: "))
discount = 0.1

if user_input >400:
    print(f"final price after discount is : {user_input - (user_input*discount)}")

else:
    print("No discount on this item. Please pay full amount or purchase anything more than 400.")