# Class List Manager - Group 10 -
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Tala","Hessa",""]


# ===== Each student adds her function BELOW this line =====

# Written by: Tala (task 1)
def count_names(names):
    return len(names)

# Written by: Hessa (task 6)
def to_upper(names):
    upper_list = []
    for name in names:
        upper_list.append(name.upper())
    return upper_list

def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Number of names:", count_names(names))
    print("Names in capital letters:", to_upper(names))


main()

