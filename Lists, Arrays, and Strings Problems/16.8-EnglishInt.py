def EnglishInt(integer):
    to_english = ''
    if integer < 0:
        to_english += 'Negative'
        integer = integer * -1

    str_version = str(integer)
    numbers = []
    for num in str_version:
        numbers.append(num)

    while len(numbers) % 3 != 0:
        numbers.insert(0, '0')
    str_version = ''.join(numbers)
    print(numbers)
    print(str_version)

    triple_pairs = len(str_version) // 3
    for i in range(len(str_version) // 3):
        print(str_version[i * 3: (i + 1) * 3])
        subsection = str_version[i * 3: (i + 1) * 3]
        to_english = Helper(triple_pairs, subsection, to_english)
        triple_pairs -= 1

    return to_english


def Helper(part, str, word):
    num_dict = {1: ' One', 2: ' Two', 3: ' Three', 4: ' Four', 5: ' Five', 6: ' Six', 7: ' Seven', 8: ' Eight',
                9: ' Nine'}
    place_dict = {0: ' Hundred', 1: 'ty', 2: ''}
    teens = {11: 'Eleven', 12: ' Twelve'}
    number = {}
    part_dict = {2: ' Thousand', 1: ''}

    for place1, num1 in enumerate(str):
        number[place1] = num1
    print(number)

    for place, num in enumerate(str):
        print(num)
        if int(num) != 0:
            print(num)
            word += num_dict[int(num)]
            word += place_dict[int(place)]
        elif num == '1' and place == 1:
            print(teens[int(num + number[2])])
            word += teens[int(num + number[2])]
            print(word)
            break
        print(word)

    word += part_dict[part]

    return word


'''
    num_dict = {1: ' One', 2: ' Two', 3: ' Three', 4: ' Four', 5: ' Five', 6: ' Six', 7: ' Seven'}
    place_dict = {0: '', 1: '', 2: '-ty', 3: ' Hundred', 4: ' Thousand'}
    elevens = {2: ' teen', 5: ' teen', 8: ' teen', 11: ' teen'}
    str_version = str(integer)
    place = len(str_version)
    string = ''
    for num in str_version:
        if int(num) == 0:
            place -= 1
            continue
        string += num_dict[int(num)] + place_dict[place]
        print(num)
        print(place)
        print(string)
        place -= 1

'''

'''    for num in str_version:
        value = len(str_version) - place
        place += 1
        zeros = value * '0'
        if num == '0':
            continue
        together = num+zeros
        string += dictionary[int(together)]
        string += ' '
        print(string)'''

x = EnglishInt(-56876)
print("THIS IS X", x)
