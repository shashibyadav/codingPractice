class MaxStocks:
    def run(self):
        prices = [7, 1, 5, 3, 6, 4]
        result = 0
        length = len(prices)
        if length == 0:
            return result
        minimum = prices[0]
        maximum = prices[0]
        isMonotonic = True

        for i in range(1, length):
            item = prices[i]
            if item < maximum:
                result += maximum - minimum
                minimum = item
                maximum = item
                isMonotonic = False
            else:
                if item < minimum:
                    result += maximum - minimum
                    minimum = item
                    maximum = item
                    isMonotonic = False
                else:
                    maximum = item

        if isMonotonic:
            result = maximum - minimum
        print(result)
        return result
