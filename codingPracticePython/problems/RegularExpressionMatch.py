class Solution:
    def helper(self, s, p, index1, index2):
        if index1 < 0 and index2 < 0:
            return True
        elif index1 < 0:
            result = True
            while index2 >= 0:
                if p[index2] != "*":
                    result = False
                    break
                index2 -= 2
            return result

        elif index2 < 0:
            return False

        s_char = s[index1]
        p_char = p[index2]
        if p_char == "." or p_char == s_char:
            return self.helper(s, p, index1 - 1, index2 - 1)
        elif p_char == "*":
            nx_index2 = index2 - 1
            if nx_index2 == -1:
                return False
            nx_p_char = p[nx_index2]
            if nx_p_char == ".":
                return True
            while nx_p_char == s_char:
                index1 -= 1
                if index1 == -1:
                    break
                s_char = s[index1]
            return self.helper(s, p, index1, index2 - 2)
        else:
            return False

    def isMatch(self, s: str, p: str) -> bool:
        length1 = len(s) - 1
        length2 = len(p) - 1
        return self.helper(s, p, length1, length2)


print(Solution().isMatch("aab", "c*a*b"))
