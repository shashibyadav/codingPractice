from collections import defaultdict


def sherlockAndAnagrams(s):
    dictionary = defaultdict(int)
    # generating substring
    length = len(s)
    count = 0
    for i in range(1, length + 1):
        for j in range(length + 1 - i):
            substring = s[j : j + i]
            substring = "".join(sorted(substring))

            count += dictionary[substring]
            dictionary[substring] += 1
    return count


print(sherlockAndAnagrams("kkkk"))
