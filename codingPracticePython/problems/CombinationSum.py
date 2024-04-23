import copy


class Solution:
    def helper(self, candidates, target, total, stack, result):
        if len(candidates) == 0:
            return
        current = candidates[0]
        # choosing the value
        stack.append(current)
        total += current
        if total == target:
            result.add(copy.deepcopy(tuple(stack)))
            stack.pop()
            total -= current
            return
        else:
            if total < target:
                self.helper(candidates[1:], target, total, stack, result)
                self.helper(candidates, target, total, stack, result)
            # not choosing the value
            stack.pop()
            total -= current
            self.helper(candidates[1:], target, total, stack, result)

    def combinationSum(self, candidates, target):
        result = set()
        stack = []
        total = 0
        self.helper(candidates, target, total, stack, result)
        return list(map(lambda x: list(x), list(result)))


print(Solution().combinationSum([2, 3, 6, 7], 7))
