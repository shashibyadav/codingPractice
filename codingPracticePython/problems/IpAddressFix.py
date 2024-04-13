class Solution:
    def restoreIpAddresses(self, s):
        result = []
        length = len(s)
        if len(s) == 0:
            return result

        self.helper(0, length - 1, 4, result, "", s)
        return result

    def helper(self, start_idx, end_idx, remaining_col, result, prefix, original):
        if start_idx > end_idx:
            return
        if remaining_col == 1:
            if (end_idx - start_idx) > 2:
                return
            else:
                s_number = original[start_idx:]
                number = int(original[start_idx:])
                if number < 255 and not (
                    s_number.startswith("0") and len(s_number) > 1
                ):
                    result.append(prefix + s_number)
                return
        s_prefix = original[start_idx : start_idx + 1]
        i_prefix = int(s_prefix)
        if i_prefix <= 255 and not (s_prefix.startswith("0") and len(s_prefix) > 1):
            self.helper(
                start_idx + 1,
                end_idx,
                remaining_col - 1,
                result,
                prefix + s_prefix + ".",
                original,
            )
        s_prefix = original[start_idx : start_idx + 2]
        i_prefix = int(s_prefix)
        if i_prefix <= 255 and not (s_prefix.startswith("0") and len(s_prefix) > 1):
            self.helper(
                start_idx + 2,
                end_idx,
                remaining_col - 1,
                result,
                prefix + s_prefix + ".",
                original,
            )
        s_prefix = original[start_idx : start_idx + 3]
        i_prefix = int(s_prefix)
        if i_prefix <= 255 and not (s_prefix.startswith("0") and len(s_prefix) > 1):
            self.helper(
                start_idx + 3,
                end_idx,
                remaining_col - 1,
                result,
                prefix + s_prefix + ".",
                original,
            )


print(Solution().restoreIpAddresses("101023"))
