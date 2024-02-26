class DFS:

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

        stack = []
        stack_set = set()
        stack.append(0)
        stack_set.add(0)
        visited = set()
        counter = 0

        while len(stack) > 0:
            node = stack.pop(-1)
            stack_set.remove(node)
            visited.add(node)
            print(node)
            for neighbor in adjList[node]:
                if neighbor not in stack_set and neighbor not in visited:
                    stack.append(neighbor)
                    stack_set.add(neighbor)

