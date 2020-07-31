"""
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z). 
"""


def StringCompression(string1):
    compressed = []
    repeat = 1
    for char in range(len(string1) - 1):
        if string1[char] == string1[char + 1]:
            repeat += 1
        else:
            compressed.append(string1[char])
            compressed.append((str(repeat)))
            repeat = 1
        last_char = string1[char + 1]
    compressed.append(last_char)
    compressed.append(str(repeat))
    if len(''.join(compressed)) < len(string1):
        return ''.join(compressed)
    return string1


""""
Time Complexity: O(n) since going through strings 
"""

"""
Space Complexity: O(n) as we are appending to a list
"""

ans1 = StringCompression('aabcccccaaa')
print(ans1)

ans2 = StringCompression('abcdefghhgfedcba')
print(ans2)

ans3 = StringCompression('asasss')
print(ans3)

ans4 = StringCompression('bccabe')
print(ans4)
