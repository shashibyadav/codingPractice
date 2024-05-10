from collections import defaultdict


def substrCount(n, s):
    dictionary = defaultdict(int)
    for char in s:
        dictionary[char] += 1
    dict_items = dictionary.items()
    counter = sum(list(map(lambda x: x[1], dict_items)))
    for item in dict_items:
        for item2 in dict_items:
            if item[0] == item2[0]:
                continue
            if item2[1] % 2 != 0:
                counter += (item2[1] - 1) // 2
            else:
                counter += item2[1] // 2
    return counter


print(substrCount(5, "abcbaba"))
