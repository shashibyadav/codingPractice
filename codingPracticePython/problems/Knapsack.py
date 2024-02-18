class Knapsack:
    def __init__(self):
        self.n = 4
        self.c = 20
        self.v = [0, 10, 2, 1, 3]
        self.w = [0, 10, 5, 10, 10]
        self.dp = {}

    def run(self):
        result = self.knapsackProblem()
        print(result)

    def worker(self, n, c):
        key = str(n) + "_" + str(c)
        if key in self.dp:
            return self.dp[key]
        result = None
        if n == 0 or c == 0:
            result = 0
        elif self.w[n] > c:
            result = self.worker(n - 1, c)
        else:
            temp1 = self.worker(n - 1, c)
            temp2 = self.v[n] + self.worker(n - 1, c - self.w[n])
            result = max(temp1, temp2)
        self.dp[key] = result
        return result

    def knapsackProblem(self):
        return self.worker(self.n, self.c)
