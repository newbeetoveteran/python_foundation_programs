#program to count number of vowels in a string
#concept : using for loop and strings

vowel_check = input("Enter the sentence: ")
vowels = "aeiouAEIOU"
vowel_count = 0
for alphabet in vowel_check:
    if alphabet in vowels:
        vowel_count += 1
print(f"Number of vowels in statenent is: {vowel_count}")