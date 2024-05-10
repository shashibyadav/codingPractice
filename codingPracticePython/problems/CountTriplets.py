from collections import defaultdict


def countTriplets(arr, r):
    dictionary = defaultdict(int)
    counter = 0
    for item in arr:
        prev_item = item / r
        if prev_item in dictionary:
            p_prev_item = prev_item / r
            if p_prev_item in dictionary:
                dictionary[item] += 1
                counter += 1 * dictionary[prev_item] * dictionary[p_prev_item]
            else:
                dictionary[item] += 1
        else:
            dictionary[item] += 1
    return counter


# print(countTriplets([1, 4, 16, 64], 4))
print(
    countTriplets(
        [1, 3, 9, 9, 27, 81],
        3,
    )
)
