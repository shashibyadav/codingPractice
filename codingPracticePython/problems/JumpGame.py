class Solution:
    def jump(self, nums):
        length = len(nums)
        if length <= 1:
            return 0
        dp = [0]
        for i in range(1, length):
            temp_min = float("inf")
            for j in range(0, i):
                distance = i - j
                capacity = nums[j]
                if capacity >= distance:
                    prev_min = dp[j]
                    temp_min = min(prev_min + 1, temp_min)

            dp.append(temp_min)

        return dp[-1]


print(Solution().jump([2, 3, 1, 1, 4]))
