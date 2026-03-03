# python program to print all even numbers from 1 to 20 using a while loop
#concept: using while loop

num = 20
i = 1
while i < num:
    if i % 2 == 0:
        print(i)
    i += 1                        #crucial as value of i must increment to check remaining numbers in the range