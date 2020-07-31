"""
 You are given two strings, pattern and value. The pattern string consists of
just the letters a and b, describing a pattern within a string. For example, the string catcatgocatgo
matches the pattern aabab (where cat is a and go is b). It also matches patterns like a, ab, and b.
Write a method to determine if value matches pattern.
"""


def PatternMatching(pattern, string):
    a_b_occurences = {}
    lst_string = []
    for letter in pattern:
        if letter in a_b_occurences:
            a_b_occurences[letter] += 1
        else:
            a_b_occurences[letter] = 1
    print(a_b_occurences)

    for i in range(0, len(string)):
        len_a = i
        len_b = (len(string) - a_b_occurences['a'] * len_a) / a_b_occurences['b']
        if len_b % 1 != 0:
            continue
        else:
            len_b = int(len_b)
        print('THIS IS ASSUMED LEN A', len_a)
        a_val = string[:len_a]
        b_val = string[len_a:len_b + 1]
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


patternmatched = PatternMatching('ababa', 'acanacana')
print(patternmatched)

patternmatched2 = PatternMatching('aabab', 'catcatgocatgo')
print(patternmatched2)


patternmatched3 = PatternMatching('ab', 'catcatgocatgo')
print(patternmatched3)

