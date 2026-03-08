#python program to print centre aligned pyramid pattern
#concept : using for loops to iterate spaces and stars

star_count = 5
star_pattern = "*"
spaces = " "
for i in range (1,star_count+1):
    print(spaces*(star_count-i) + star_pattern*(2*i-1))