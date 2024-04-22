class Solution:
    def binary_search(self, nums, start, end, target):
        if start == end:
            if nums[start] == target:
                return start
            else:
                return -1
        mid = start + (end - start) // 2
        mid_value = nums[mid]
        if mid_value > target:
            return self.binary_search(nums, start, mid, target)
        elif mid_value == target:
            return mid
        else:
            return self.binary_search(nums, mid + 1, end, target)

    def searchRange(self, nums, target):
        length = len(nums)
        index = self.binary_search(nums, 0, length - 1, target)
        if index == -1:
            return [-1, -1]
        first = index
        second = index
        while first >= 0 and nums[first] == target:
            first -= 1
        while second < length - 1 and nums[second] == target:
            second += 1
        return [first + 1, second - 1]


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
