class LongestSubstringWithoutRepeating:

    def run(self):
        s = "abcabcbb"
        # s = " "
        # s = "pwwkew"
        # s = "abba"
        pointer1 = 0
        pointer2 = 0
        longest = 0
        characters = dict()
        while pointer2 <= len(s) - 1:
            character = s[pointer2]

            if character in characters:
                if characters[character] >= pointer1:
                    pointer1 = characters[character] + 1

            longest = max((pointer2 - pointer1) + 1, longest)
            characters[character] = pointer2
            pointer2 += 1

        print(longest)
        return longest