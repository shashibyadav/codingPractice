from collections import defaultdict


def freqQuery(queries):
    dictionary = defaultdict(int)
    inverted_dict = defaultdict(set)
    result = []
    for query in queries:
        q = query[0]
        var = query[1]
        if q == 1:
            inverted_dict[dictionary[var]].discard(var)
            dictionary[var] += 1
            inverted_dict[dictionary[var]].add(var)
        elif q == 2:
            inverted_dict[dictionary[var]].discard(var)
            dictionary[var] -= 1
            inverted_dict[dictionary[var]].add(var)
        else:
            if var in inverted_dict and len(inverted_dict[var]) > 0:
                result.append(1)
            else:
                result.append(0)
    return result


queries = [[1, 1], [2, 2], [3, 2], [1, 1], [1, 1], [2, 1], [3, 2]]

print(freqQuery(queries))
