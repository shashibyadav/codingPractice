def mergeSort(arr, result_f):
    if len(arr) == 1:
        return arr
    if len(arr) == 0:
        return []

    length = len(arr) - 1
    median = length // 2

    left = mergeSort(arr[0 : median + 1], result_f)
    right = mergeSort(arr[median + 1 :], result_f)
    first = 0
    second = 0
    result = []
    while first < len(left) and second < len(right):
        first_v = left[first]
        second_v = right[second]
        if first_v < second_v:
            result.append(first_v)
            first += 1
        else:
            result.append(second_v)
            second += 1
            result_f["count"] += len(left) - first
    while first < len(left):
        result.append(left[first])
        first += 1

    while second < len(right):
        result.append(right[second])
        second += 1

    return result


def countInversions(arr):
    # Write your code here
    result_f = dict()
    result_f["count"] = 0

    sorted_arr = mergeSort(arr, result_f)
    return sorted_arr


print(countInversions([2, 4, 1]))
