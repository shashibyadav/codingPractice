from bisect import bisect, bisect_left


def activityNotifications(expenditure, d):
    # Write your code here
    notifications = 0
    length = len(expenditure)
    sorted_arr = sorted(expenditure[0:d])
    for i in range(d, length):
        start = i - d
        end = i - 1
        first = expenditure[start]
        last = expenditure[end]
        current_value = expenditure[i]

        median = 0
        if d % 2 == 0:
            med_index = (d - 1) // 2
            median = (sorted_arr[med_index] + sorted_arr[med_index + 1]) / 2
        else:
            med_index = (d - 1) // 2
            median = sorted_arr[med_index]
        if current_value >= (2 * median):
            notifications += 1

        del_index = bisect(sorted_arr, first) - 1
        sorted_arr.pop(del_index)
        ins_index = bisect_left(sorted_arr, current_value)
        sorted_arr.insert(ins_index, current_value)

    return notifications


print(activityNotifications([10, 20, 30, 40, 50], 3))
