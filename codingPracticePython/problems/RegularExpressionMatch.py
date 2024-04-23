class Solution:
    def helper(self, s, p, index1, index2, dp):
        if index1 < 0 and index2 < 0:
            return True
        key = f"{index1}_{index2}"
        if index1 < 0:
            return dp[key]
        if index2 < 0:
            return False
        if key in dp:
            return dp[key]
        p_char = p[index2]
        s_char = s[index1]
        result = False
        if p_char == "." or p_char == s_char:
            result = self.helper(s, p, index1 - 1, index2 - 1, dp)
        elif p_char == "*":
            nx_p_char = p[index2 - 1]
            if nx_p_char == s_char or nx_p_char == ".":
                result = self.helper(s, p, index1 - 1, index2, dp)
                result2 = self.helper(s, p, index1 - 1, index2 - 2, dp)
                result3 = self.helper(s, p, index1, index2 - 2, dp)
                result = result or result2 or result3
            else:
                result = self.helper(s, p, index1, index2 - 2, dp)
        dp[key] = result
        return result

    def isMatch(self, s: str, p: str) -> bool:
        length1 = len(s) - 1
        length2 = len(p) - 1
        dp = dict()
        dp["-1_-1"] = True
        start = 0
        while start <= length2:
            item = p[start]
            dp[f"-1_{start}"] = False
            if start + 1 <= length2:
                item2 = p[start + 1]
                if item2 == "*":
                    dp[f"-1_{start + 1}"] = True and dp[f"-1_{start - 1}"]
                    start = start + 2
                else:
                    start += 1
            else:
                start += 1
        return self.helper(s, p, length1, length2, dp)


print(Solution().isMatch("a", "..*"))
