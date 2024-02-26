class NetworkFlow:

    def bfs(self, adjList, startNode, endNode):
        print()
    def run(self):
        input = [(0,1,16), (0,2,13), (1,2,10),
                 (2,1,4), (1,3,12), (2,4,14),
                 (3,2,9), (4,3,7), (3,5,20),
                 (4,5,4)]

        adjList = dict()
        weights = dict()
        flows = dict()

        initial = 0
        sink = 5

        for edge in input:
            start = edge[0]
            end = edge[1]
            weight = edge[2]
            if start not in adjList:
                adjList[start] = set()
            if end not in adjList:
                adjList[end] = set()
            key = str(start) + "-" + str(end)
            weights[key] = weight
            flows[key] = 0



