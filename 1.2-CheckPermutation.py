"""
Given two strings, write a method to decide if one is a permutation of the
other.
"""


def CheckPermutation(str1, str2):
    # we know that if the strings are of different length they can not be permutations of each other.
    # Assumption: CASE SENSITIVE
    if len(str1) > len(str2) or len(str1) < len(str2):
        return False
    str1d = {}
    str2d = {}
    for char in range(len(str1)):
        if str1[char] in str1d:
            str1d[str1[char]] += 1
        else:
            str1d[str1[char]] = 1
        if str2[char] in str2d:
            str2d[str2[char]] += 1
        else:
            str2d[str2[char]] = 1
    return str1d == str2d


""""
Assume that the length of the strings are equal n. Then in the worst case, we go through each letter in string, or O(n).
We then compare the dictionaries which is also O(n). O(n) + O(n) = O(2n) but constants get dropped.
Time Complexity: O(n)
"""

"""
Adding a dictionary, and at worse case we would have to input n letters.
Space Complexity: O(n)
"""


ans1 = CheckPermutation('abcdefg', 'Gdcba')
print(ans1)

ans2 = CheckPermutation('cat', 'tac')
print(ans2)

ans3 = CheckPermutation('loppp', 'poplp')
print(ans3)

ans4 = CheckPermutation('DOG', 'ogd')
print(ans4)
