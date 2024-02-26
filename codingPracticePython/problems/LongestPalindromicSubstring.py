class LongestPalindromicSubstring:

    def run(self):
        s = "bb"
        longest = 0
        result = ""
        if len(s) == 1:
            return s
        for i in range(1, len(s) + 1):
            for j in range(0, len(s) - i + 1):
                temp = s[j:j + i]
                if temp == temp[::-1]:
                    if i > longest:
                        longest = i
                        result = temp
        print(result)