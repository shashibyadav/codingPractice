import copy


class Solution:
    def subsets(self, nums):
        length = len(nums)
        if length == 0:
            return []
        result = [[]]
        self.helper(0, result, nums, [])
        return result

    def helper(self, index, result, nums, prev_subset):
        if index >= len(nums):
            return
        # not selected
        current_subset = copy.deepcopy(prev_subset)
        self.helper(index + 1, result, nums, current_subset)
        # result.append(copy.deepcopy(current_subset))
        # selected
        current_subset.append(nums[index])
        self.helper(index + 1, result, nums, copy.deepcopy(current_subset))
        result.append(copy.deepcopy(current_subset))


print(Solution().subsets([1, 2, 3]))
