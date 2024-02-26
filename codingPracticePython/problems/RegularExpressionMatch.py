class RegularExpressionMatch:

    def run(self):
        s = "aab"
        p = "c*a*b"
        pointer1 = 0
        pointer2 = 0
        result = True
        while pointer1 < len(s) and pointer2 < len(p):
            chars = s[pointer1]
            charp = p[pointer2]
            if charp == ".":
                pointer1 += 1
                pointer2 += 1
                continue
            if charp == "*":
                prevchar = p[pointer2 - 1]
                if prevchar == ".":
                    pointer1 = len(s)
                    pointer2 += 1
                    break

                while pointer1 < len(s) and prevchar == s[pointer1]:
                    pointer1 += 1
                pointer2 += 1
                continue
            if charp == chars:
                pointer1 += 1
                pointer2 += 1
                continue
            result = False
            break
        if pointer2 < len(p):
            result = False
        if pointer1 < len(s):
            result = False
        print(result)
        return result