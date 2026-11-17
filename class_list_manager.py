# Class List Manager - Group 10 -
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Tala","Hessa",""]


# ===== Each student adds her function BELOW this line =====

# Written by: Tala (task 7)
def count_vowels(name):
    vowels = "aeiou"                     # variable: the vowel letters
    count = 0                            # variable: number of vowels found
    for letter in name.lower():          # loop: check each letter in the name
        if letter in vowels:             # if: the letter is a vowel
            count += 1                   # increase the vowel count
    return count                         # return the total number of vowels

# Written by: Hessa (task 6)
def to_upper(names):
    upper_list = []                      # variable: new empty list
    for name in names:                   # loop: check every name in the list
        upper_list.append(name.upper())  # add the name in capital letters
    return upper_list

def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Number of vowels:", count_vowels(names[0]))
    print("Names in capital letters:", to_upper(names))


main()

