def alternatingCharacters(s):
    # Write your code here
    length = len(s)
    counter = 0
    for i in range(length - 1, 0, -1):
        first = s[i - 1]
        second = s[i]
        if first == second:
            s = s[0 : len(s) - 1]
            counter += 1
    return counter


print(alternatingCharacters("ABABABA"))
