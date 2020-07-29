"""
Given a string, write a function to check if it is a permutation of
a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
permutation is a rearrangement of letters. The palindrome does not need to be limited to just
dictionary words. 
"""


def PalindromePerm(str1):
    occurences = {}
    for char in str1:
        if char in occurences:
            occurences[char] += 1
        else:
            occurences[char] = 1
    if len(str1) % 2 == 0:
        for letter in occurences:
            if occurences[letter] % 2 != 0:
                return False
            else:
                return True
    OddsAllowed = 1
    for lett in occurences:
        if occurences[lett] % 2 != 0:
            OddsAllowed = OddsAllowed - 1
    return OddsAllowed < 0
