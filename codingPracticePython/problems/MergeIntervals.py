class Solution:
    def merge(self, intervals):
        length = len(intervals)
        intervals = sorted(intervals, key=lambda x: x[1])
        for i in range(length - 2, -1, -1):
            current = intervals[i]
            previous = intervals[i + 1]
            if (
                previous[0] <= current[0] <= previous[1]
                or previous[0] <= current[1] <= previous[1]
                or current[0] <= previous[0] <= current[1]
                or current[0] <= previous[1] <= current[1]
            ):
                new_interval = [
                    min(current[0], previous[0]),
                    max(current[1], previous[1]),
                ]
                intervals.pop(i + 1)
                intervals.pop(i)
                intervals.insert(i, new_interval)

        return intervals


print(Solution().merge([[1, 4], [0, 2], [3, 5]]))
