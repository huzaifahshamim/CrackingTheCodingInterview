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

    true_length = len(str1)
    if ' ' in occurences:
        true_length = len(str1) - occurences[' ']
        del occurences[' ']

    if true_length % 2 == 0:
        for letter in occurences:
            if occurences[letter] % 2 != 0:
                return False
        return True

    OddsAllowed = 1
    for lett in occurences:
        if occurences[lett] % 2 != 0:
            OddsAllowed = OddsAllowed - 1
    return OddsAllowed >= 0


""""
Since we are using a dictionary. TC will be O(true_length) + O(len(modified)) due to the .join. The length of
modified will be larger than true_length. 
Time Complexity: O(len(modified))
"""

"""
Using a list and appending values to it.
Space Complexity: ~O(n)
"""

ans1 = PalindromePerm('tact coa')
print(ans1)

ans2 = PalindromePerm('what is popp in')
print(ans2)

ans3 = PalindromePerm('hello ')
print(ans3)

ans4 = PalindromePerm('aboba')
print(ans4)
