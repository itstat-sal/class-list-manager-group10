# Class List Manager - Group 10 -
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Tala","Hessa","Kadi"]


# ===== Each student adds her function BELOW this line =====

# Written by: Tala (task 7)
def count_vowels(name):
    vowels = "aeiou"                     # variable: vowel letters
    count = 0                            # variable: number of vowels
    for letter in name.lower():          # loop: check each letter
        if letter in vowels:             # if: this letter is a vowel
            count += 1                   # increase the count
    return count                         # return the total number


# Written by: Hessa (task 6)
def to_upper(names):
    upper_list = []                      # variable: new empty list
    for name in names:                   # loop: check every name in the list
        upper_list.append(name.upper())  # add the name in capital letters
    return upper_list


# Written by: Kadi (task 3)
def sort_names(names):                   # function: sort the names alphabetically
sorted_names = sorted(names)             # variable: store the sorted names
return sorted_names                      # return the sorted list

def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Vowel count for each name:", [(name, count_vowels(name)) for name in names])
    print("Names in capital letters:", to_upper(names))
    print("Sorted names:", sort_names(names))

main()

