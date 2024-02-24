import heapq


class GoldmanSachs:

    def getMinMax(self, minHeap, maxHeap, elements):
        total = None
        while True:
            minimum = heapq.heappop(minHeap)
            maximum = heapq.heappop(maxHeap)
            if minimum not in elements:
                heapq.heappush(maxHeap, maximum)
                continue
            if (-1 * maximum) not in elements:
                heapq.heappush(minHeap, minimum)
                continue
            total = minimum * (-1 * maximum)
            heapq.heappush(minHeap, minimum)
            heapq.heappush(maxHeap, maximum)
            break
        return total



    def run(self):
        operations = ["push","push","push","pop"]
        x = [1,2,3,1]
        # operations = ["push","push"]
        # x = [3,2]

        elements = set()
        minHeap = []
        maxHeap = []
        result = []
        for i in range(len(x)):
            tempX = x[i]
            tempOperation = operations[i]
            if tempOperation == "push":
                elements.add(tempX)
                heapq.heappush(minHeap, tempX)
                heapq.heappush(maxHeap, -1 * tempX)
                ans = self.getMinMax(minHeap, maxHeap, elements)
                result.append(ans)
            elif tempOperation == "pop":
                elements.remove(tempX)
                ans = self.getMinMax(minHeap, maxHeap, elements)
                result.append(ans)

        print(result)
