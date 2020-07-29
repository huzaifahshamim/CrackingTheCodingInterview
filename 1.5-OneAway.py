"""
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
"""


def OneAway(string1, string2):
    # first check if they are more than one edit way from each other, i.e. the length difference is greater than one
    str1 = len(string1)
    str2 = len(string2)
    if str1 - 2 >= str1 or str1 + 2 <= str2:
        return False

    if str1 == str2:
        EditsAway = 0
        for i in range(str1):
            if string1[i] != string2[i]:
                EditsAway += 1
        return EditsAway <= 1

    elif str1 > str2:
        bigger_str = string1
        smaller_str = string2
    else:
        bigger_str = string2
        smaller_str = string1

    chars = []
    bigger_char = []
    for letter1 in bigger_str:
        chars.append(letter1)
        bigger_char.append(letter1)
    for letter2 in smaller_str:
        try:
            chars.remove(letter2)
        except:
            continue
    if len(chars) > 1:
        return False
    else:
        bigger_char.remove(chars[0])
        return ''.join(bigger_char) == smaller_str

ans1 = OneAway('pale','ple')
print(ans1)

ans2 = OneAway('pales', 'pale')
print(ans2)

ans3 = OneAway('pale','bale')
print(ans3)

ans4 = OneAway('pale','bae')
print(ans4)

ans4 = OneAway('sale','sael')
print(ans4)


