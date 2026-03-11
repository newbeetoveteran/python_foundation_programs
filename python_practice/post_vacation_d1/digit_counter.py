#digit counter python program
#using concept of dictionary and for loop

number = "112233444555688"
digit_count = {}
for i in number:
    if i in digit_count:
        digit_count [i] += 1
    else:
        digit_count[i] = 1
for digit in digit_count:
    print(f"{digit} appears {digit_count[digit]} times")