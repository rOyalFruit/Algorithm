from collections import deque


def bfs(si, sj, maps, visited):
    result = int(maps[si][sj])
    q = deque([(si, sj)])
    visited[si][sj] = True
    
    while q:
        ci, cj = q.popleft()
        
        for di, dj in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            ni = ci + di
            nj = cj + dj
            
            if 0 <= ni < len(maps) and 0 <= nj < len(maps[ci]) and not visited[ni][nj] and maps[ni][nj] != 'X':
                q.append((ni, nj))
                visited[ni][nj] = True
                result += int(maps[ni][nj])
        
    return result


def solution(maps):
    answer = []
    visited = [[False for _ in range(len(maps[i]))] for i in range(len(maps))]

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(i, j, maps, visited))
                              
    return sorted(answer) if answer else [-1]
                              