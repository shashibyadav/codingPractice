class Solution:
    def prefixScores(self, arr):
        result = [0]
        length = len(arr)
        M = int(1e9) + 7
        prefix_sum = 0
        for i in range(1, length + 1):
            prefix_sum = (prefix_sum + arr[i - 1]) % M
            new_result = (prefix_sum + (i * arr[i - 1])) % M
            result.append(new_result)
        return result[1:]


print(Solution().prefixScores([1, 2, 3]))
