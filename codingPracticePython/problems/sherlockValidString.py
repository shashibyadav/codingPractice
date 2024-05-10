from collections import defaultdict


def isValid(s):
    # Write your code here
    dictionary = defaultdict(int)
    for item in s:
        dictionary[item] += 1
    final_l = list(map(lambda x: x[1], dictionary.items()))
    dictionary_2 = defaultdict(int)
    for item in final_l:
        dictionary_2[item] += 1
    final_l = list(map(lambda x: x[1], dictionary_2.items()))
    if len(final_l) > 2:
        return "NO"
    elif len(final_l) == 1:
        return "YES"
    elif final_l[0] == 1 or final_l[1] == 1:
        return "YES"
    else:
        return "NO"


print(isValid("aaaabbcc"))
