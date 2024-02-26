import copy


class LetterCombinations:

    def run(self):
        digits = "23"
        queue = None
        dictionary = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        for i in range(len(digits)):
            digit = digits[i]
            if queue is None:
                queue = copy.deepcopy(dictionary[digit])
                continue
            length = len(queue)
            for i in range(length):
                poped = queue.pop(0)
                for item in dictionary[digit]:
                    queue.append(poped + item)

        print(queue)
