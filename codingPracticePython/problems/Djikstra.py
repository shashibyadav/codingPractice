import heapq


class Djikstra:

    def run(self):
        input = [
            (0,1,4), (0,7,8), (1,7,11),
            (1,2,8), (7,8,7), (7,6,1),
            (2,8,2), (8,6,6), (6,5,2),
            (2,5,4), (2,3,7), (3,5,14),
            (3,4,9), (5,4,10)
        ]

        adjList = dict()
        weights = dict()
        nodes = set()
        path_distances = dict()

        # making adjacency lists
        for item in input:
            start = item[0]
            end = item[1]
            value = item[2]
            key1 = str(start) + "_" + str(end)
            key2 = str(end) + "_" + str(start)
            if start not in adjList:
                adjList[start] = set()
            if end not in adjList:
                adjList[end] = set()

            adjList[start].add(end)
            adjList[end].add(start)
            weights[key1] = value
            weights[key2] = value
            nodes.add(start)
            nodes.add(end)

        for node in nodes:
            # starting node
            if node == 0:
                path_distances[node] = 0
            else:
                path_distances[node] = float("inf")

        # algorithm
        # visited = set()
        # visited.add(0)
        min_heap = []
        heapq.heappush(min_heap, (0, 0))

        while len(min_heap) > 0:
            dist, start = heapq.heappop(min_heap)
            for end in adjList[start]:
                key = str(start) + "_" + str(end)
                weight = dist + weights[key]
                if path_distances[end] > weight:
                    path_distances[end] = weight
                    heapq.heappush(min_heap, (weight, end))


        print(path_distances)