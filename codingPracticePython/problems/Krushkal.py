import heapq


class Krushkal:

    def run(self):
        input = [
            (0, 1, 4), (0, 7, 8), (1, 7, 11),
            (1, 2, 8), (7, 8, 7), (7, 6, 1),
            (2, 8, 2), (8, 6, 6), (6, 5, 2),
            (2, 5, 4), (2, 3, 7), (3, 5, 14),
            (3, 4, 9), (5, 4, 10)
        ]

        # making min_heap

        min_heap = []
        selected_edges = []
        set_dictionary = dict()
        for start, end, weight in input:
            heapq.heappush(min_heap, (weight, start, end))
            if start not in set_dictionary:
                set_dictionary[start] = set()
                set_dictionary[start].add(start)
            if end not in set_dictionary:
                set_dictionary[end] = set()
                set_dictionary[end].add(end)

        while len(min_heap) > 0:
            weight, start, end = heapq.heappop(min_heap)
            if set_dictionary[start] != set_dictionary[end]:
                temp_set = set_dictionary[start].union(set_dictionary[end])
                for item in temp_set:
                    set_dictionary[item] = temp_set
                selected_edges.append((start, end))

        print(selected_edges)

