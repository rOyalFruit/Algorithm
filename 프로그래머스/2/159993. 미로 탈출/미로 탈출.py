from collections import deque


def bfs(si, sj, ei, ej, maps):
    visited = [[-1 for _ in range(len(maps[i]))] for i in range(len(maps))]
    q = deque([(si, sj)])
    visited[si][sj] = 0

    while q:
        ci, cj = q.popleft()
        
        if (ci, cj) == (ei, ej):
            return visited[ei][ej]

        for di, dj in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            ni = ci + di
            nj = cj + dj
            
            if 0 <= ni < len(maps) and 0 <= nj < len(maps[ni]) and maps[ni][nj] != 'X' and visited[ni][nj] == -1:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
    return -1


def solution(maps):
    si, sj = -1, -1  # 시작 좌표
    li, lj = -1, -1  # 레버 좌표
    ei, ej = -1, -1  # 출구 좌표
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                si, sj = i, j
            if maps[i][j] == 'L':
                li, lj = i, j
            if maps[i][j] == 'E':
                ei, ej = i, j
                
    s_to_l = bfs(si, sj, li, lj, maps)  # 시작 지점 -> 레버까지 거리
    l_to_e = bfs(li, lj, ei, ej, maps)  # 레버 -> 출구까지 거리
    
    if s_to_l == -1 or l_to_e == -1:
        return -1

    return s_to_l + l_to_e