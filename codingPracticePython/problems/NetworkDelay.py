import heapq


class NetworkDelaySolution:
    def run(self):
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        n = 4
        k = 2
        print(self.networkDelayTime(times, n, k))

    def networkDelayTime(self, times: [[int]], n: int, k: int) -> int:
        # generating graph
        graph = [[float("inf") for i in range(n)] for i in range(n)]

        for item in times:
            source = item[0] - 1
            dest = item[1] - 1
            graph[source][dest] = item[2]

        # algorithm start
        starting_node = k - 1

        distances = {vertex: float("infinity") for vertex in range(n)}
        distances[starting_node] = 0
        predecessors = {vertex: None for vertex in range(n)}

        # Use a priority queue to track the vertices with their distances
        priority_queue = [(0, starting_node)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbour in range(n):
                weight = graph[current_vertex][neighbour]
                distance = current_distance + weight

                if distance < distances[neighbour]:
                    distances[neighbour] = distance
                    predecessors[neighbour] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbour))

        highestTime = float("-inf")
        for vertex, distance in distances.items():
            if distance > highestTime:
                highestTime = distance
        if highestTime == float("inf"):
            return -1
        else:
            return highestTime
