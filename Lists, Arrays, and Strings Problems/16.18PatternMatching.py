"""
 You are given two strings, pattern and value. The pattern string consists of
just the letters a and b, describing a pattern within a string. For example, the string catcatgocatgo
matches the pattern aabab (where cat is a and go is b). It also matches patterns like a, ab, and b.
Write a method to determine if value matches pattern.
"""


def PatternMatching(pattern, string):
    if len(pattern) == 1:
        return True
    if len(pattern) == 2 and pattern[0] != pattern[1]:
        return True

    a_b_occurences = {}
    for letter in pattern:
        if letter in a_b_occurences:
            a_b_occurences[letter] += 1
        else:
            a_b_occurences[letter] = 1

    print("OCCURENCE", a_b_occurences)
    a_or_b = 'ab'
    a_or_b = a_or_b.replace(pattern[0], '')

    first_one = pattern[0]
    print('FIRST LETTER', first_one)

    second_one = 'a' if first_one == 'b' else 'b'

    for i in range(1, len(string)):
        len_first = i
        print('ASSUMED LENGTH', len_first)
        if first_one == 'a':
            print('STRING', string, len(string))
            print("TIMES SHOW UP", a_b_occurences['a'] * len_first)
            print("TIMES SHOW UP OTHER", a_b_occurences['b'])
            len_second = (len(string) - a_b_occurences['a'] * len_first) / a_b_occurences['b']
        else:
            len_second = (len(string) - a_b_occurences['b'] * len_first) / a_b_occurences['a']
        print('SECOND LENGTH', len_second)

        if len_second % 1 != 0 or len_second < 0:
            continue
        else:
            len_second = int(len_second)
        print("DEF INT" , len_first,len_second)

        lengths = {first_one: len_first, second_one: len_second}
        print(lengths)

        patterns = {}
        prev = 0
        next = 0
        flag = True
        for j in range(len(pattern)):
            print(j)
            print(pattern[j])
            print(patterns)
            next = lengths[pattern[j]] + next
            if pattern[j] in patterns:
                if string[prev:next] != patterns[pattern[j]]:
                    break
            else:
                patterns[pattern[j]] = string[prev:next]
            prev = next
        if flag:
            return True
    return False



'''

        for j in range(len(pattern) - 1):
            next = lengths[pattern[j]] + next
            if pattern[j] in patterns:
                if string[prev:next] != patterns[j]:
                    break
                else:
                    continue
            else:
                patterns[j] = string[prev:next]
            prev = next
'''

'''
        print("THIS IS A", a_val)
        print("THIS IS B", b_val)
        for char in pattern:
            if char == 'a':
                lst_string.append(a_val)
            else:
                lst_string.append(b_val)
        if ''.join(lst_string) == string:
            return True
    return False
'''

x = PatternMatching('aab', 'acanacana')
print(x)

'''
patternmatched = PatternMatching('ababa', 'acanacana')
print(patternmatched)

patternmatched2 = PatternMatching('aabab', 'catcatgocatgo')
print(patternmatched2)

patternmatched3 = PatternMatching('ab', 'catcatgocatgo')
print(patternmatched3)
'''
