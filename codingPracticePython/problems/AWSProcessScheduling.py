import heapq
import math
from queue import PriorityQueue

import heapdict


class AWSProcessScheduling:
    def __init__(self):
        self.priority = None

    def run(self):
        input = [6, 6, 6, 1, 2, 2]
        dictionary = dict()

        for i in range(len(input)):
            if input[i] not in dictionary:
                dictionary[input[i]] = []
            heapq.heappush(dictionary[input[i]], i)
        indexes_to_pop = set()
        while True:
            # finding max shared priority
            key = -1
            max = float("-Inf")
            for item, indexList in dictionary.items():
                count = len(indexList)
                if count > max:
                    max = count
                    key = item
            if max <= 1:
                break
            indexes = dictionary[key]
            index1 = heapq.heappop(indexes)
            index2 = heapq.heappop(indexes)
            # input.pop(index1)
            indexes_to_pop.add(index1)
            newPriority = math.floor(key / 2)
            if newPriority not in dictionary:
                dictionary[newPriority] = []
            heapq.heappush(dictionary[newPriority], index2)
            input[index2] = newPriority

        final = []
        for i in range(len(input)):
            if i in indexes_to_pop:
                continue
            final.append(input[i])
        print(final)
        return final
