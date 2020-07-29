"""Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?"""


def IsUnique(string):
    characters = {}  # create empty dictionary to keep track of each letter
    # following for loop basically checks to see if a letter is already in the dictionary. if it is, then we knoe
    # that we dont have a unique string. If it is not, then we add it to the dictionary
    for letter in string:
        if letter in characters:
            return False
        else:
            characters[letter] = True
    return True


ans1 = IsUnique('abcdg')
print(ans1)

ans2 = IsUnique('a1234567890g1h')
print(ans2)

ans3 = IsUnique('124390')
print(ans3)

ans4 = IsUnique('abcdipkha')
print(ans4)

