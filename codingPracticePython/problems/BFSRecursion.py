class BFSRecursion:

    def bfs(self, adjList, currentNode, visited):
        print()

    def run(self):

        input = [
            (0, 1, 4), (0, 7, 8), (1, 7, 11),
            (1, 2, 8), (7, 8, 7), (7, 6, 1),
            (2, 8, 2), (8, 6, 6), (6, 5, 2),
            (2, 5, 4), (2, 3, 7), (3, 5, 14),
            (3, 4, 9), (5, 4, 10)
        ]

        adjList = dict()
        nodes = set()

        for edge in input:
            start = edge[0]
            end = edge[1]
            if start not in adjList:
                adjList[start] = set()

            if end not in adjList:
                adjList[end] = set()
            adjList[start].add(end)
            nodes.add(start)
            nodes.add(end)

        visited = set()
        self.bfs(adjList, 0,visited)
