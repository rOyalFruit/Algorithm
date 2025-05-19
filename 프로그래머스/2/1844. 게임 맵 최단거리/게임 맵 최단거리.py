from collections import deque

def solution(maps):
    q = deque()
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited[0][0] = 1
    q.append((0, 0))

    while q:
        ci, cj = q.popleft()

        if ci == len(maps) - 1 and cj == len(maps[0]) - 1:
            return visited[ci][cj]

        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni = ci + di
            nj = cj + dj

            if (0 <= ni < len(maps) and 0 <= nj < len(maps[0]) and maps[ni][nj] == 1 and visited[ni][nj] == 0):
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1

    return -1
