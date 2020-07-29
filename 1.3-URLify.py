"""
Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: if implementing in Java, please use a character array so that you can
perform this operation in place.)
"""


def URLify(str1, true_length):
    modified = []
    for place in range(true_length):
        if str1[place] == ' ':
            modified.append('%20')
        else:
            modified.append(str1[place])
    back_to_str = ''.join(modified)
    return back_to_str


ans1 = URLify('Mr John Smith        ', 13)
print(ans1)

ans2 = URLify('what is popp in', 15)
print(ans2)

ans3 = URLify('hello ', 6)
print(ans3)

ans4 = URLify(' DOG', 4)
print(ans4)