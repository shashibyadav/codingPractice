def explore(n, m, obstacles, teleports, visited, row, col):
    row, col = 0, 0

    while row < n:
        if (row, col) in obstacles:
            return (row, col)

        if (row, col) in teleports:
            row, col = teleports[(row, col)]
            continue

        col += 1

        if col == m:
            col = 0
            row += 1

    return (n - 1, m - 1)


n = 3
m = 4
obstacles = [[2, 0], [2, 1]]
teleports = [[1, 2, 1, 1], [1, 3, 2, 2]]


def solution(n, m, obstacles, teleports):
    obs_t = []
    for item in obstacles:
        obs_t.append((item[0], item[1]))
    dictionary = dict()
    for item in teleports:
        dictionary[(item[0], item[1])] = (item[2], item[3])
    result = explore(n, m, obs_t, dictionary)
    print(result == (n - 1, m - 1))
    print(result)


solution(n, m, obstacles, teleports)
