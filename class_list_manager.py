# Class List Manager - Group 10 -
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Tala","Hessa",""]


# ===== Each student adds her function BELOW this line =====

# Written by: Tala (task 4)
def longest_name(names):
    longest = names[0]                  # variable: the longest name so far
    for name in names:                  # loop: check every name in the list
        if len(name) > len(longest):    # if: this name is longer
            longest = name              # update the longest name
    return longest                      # return the longest name found

# Written by: Hessa (task 6)
def to_upper(names):
    upper_list = []                      # variable: new empty list
    for name in names:                   # loop: check every name in the list
        upper_list.append(name.upper())  # add the name in capital letters
    return upper_list

def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Longest name:", longest_name(names))
    print("Names in capital letters:", to_upper(names))


main()

