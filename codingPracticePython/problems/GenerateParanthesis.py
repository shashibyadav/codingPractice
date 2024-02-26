import copy


class GenerateParenthesis:

    def generateParenthesisRun(self, dictionary, startCounter, endCounter):
        result = []
        key = str(startCounter) + "-" + str(endCounter)
        if key in dictionary:
            return copy.deepcopy(dictionary[key])
        if endCounter == 0:
            if startCounter == 0:
                result.append("")
            else:
                temp = ""
                for i in range(startCounter):
                    temp += "("
                result.append(temp)
        elif startCounter == 0:
            temp = ""
            for i in range(endCounter):
                temp += ")"
            result.append(temp)
        elif startCounter == endCounter:
            result_t = self.generateParenthesisRun(dictionary, startCounter, endCounter - 1)
            for item in result_t:
                result.append(item + ")")
        else:
            result_t = self.generateParenthesisRun(dictionary, startCounter - 1, endCounter)
            for item in result_t:
                result.append(item + "(")
            result_t = self.generateParenthesisRun(dictionary, startCounter, endCounter - 1)
            for item in result_t:
                result.append(item + ")")

        dictionary[key] = copy.deepcopy(result)

        return result

    # def generateParenthesis(self, unique_comb, count):
    #     queue = [""]
    #     length = 1
    #     for i in range(count):
    #         hash_set = set()
    #         for j in range(length):
    #             poped = queue.pop(0)
    #



    def run(self):
        n = 3
        dictionary = dict()
        result = self.generateParenthesisRun(dictionary, n, n)
        print(result)
