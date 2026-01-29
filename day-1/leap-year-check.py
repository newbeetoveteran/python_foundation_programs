#leap year checker
#concept - if the year is divisible by 4, it is a leap year using if else statements
year = int(input("Enter the year to check if it's a leap year: "))

if year %4 ==0:
    print("Entered year is a leap year.")
else:
    print("Entered year is not a leap year.")