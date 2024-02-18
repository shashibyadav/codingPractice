def run():
    # numCourses = 2
    # prerequisites = [[0, 1]]
    # result = canFinish(numCourses, prerequisites)
    # print(result)
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge(intervals))


def canFinish(numCourses: int, prerequisites: [[int]]) -> bool:
    graph = {}
    nodeInDegress = {}
    for i in range(numCourses):
        graph[i] = []
        nodeInDegress[i] = 0
    for item in prerequisites:
        course = item[0]
        preReq = item[1]
        graph[preReq].append(course)
        nodeInDegress[course] += 1

    startNodes = []
    for node in range(numCourses):
        if nodeInDegress[node] == 0:
            startNodes.append(node)

    visited = set()
    for start in startNodes:
        # running dfs
        stack = []
        stack.append(start)
        while len(stack) > 0:
            node = stack.pop()
            visited.add(node)
            for child in graph[node]:
                nodeInDegress[child] -= 1
                if nodeInDegress[child] == 0:
                    stack.append(child)

    return len(visited) == numCourses


def merge(intervals: [[int]]) -> [[int]]:
    intervals.sort()
    for i in range(1, len(intervals)):
        first = intervals[i - 1]
        sec
        if
    for nextInterval in intervals[1:]:
        top = stack[-1]
        if top[0] <= nextInterval[0] <= top[1]:
            top[1] = max(top[1], nextInterval[1])
        else:
            stack.append(nextInterval)

    return stack


# def dfs_visit(node, stack, nodeInDegress, visited, graph):
#     if node in visited and nodeInDegress[node] == 0:
#         raise Exception("cycle detected")
#     stack.append(node)
#     for child in graph[node]:
#         dfs_visit(child, stack, stackMap, visited, graph)
#     visited.add(node)
#     stack.pop()

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)