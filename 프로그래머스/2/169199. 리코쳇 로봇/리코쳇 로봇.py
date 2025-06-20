from collections import deque


def bfs(si, sj, board):
    n, m = len(board), len(board[0])
    visited = [[-1] * m for _ in range(n)]
    visited[si][sj] = 0
    q = deque([(si, sj)])
    
    while q:
        ci, cj = q.popleft()

        if board[ci][cj] == 'G':
            return visited[ci][cj]
        
        for di, dj in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            ni, nj = ci, cj
            while True:
                ni += di
                nj += dj
                
                if not (0 <= ni < n and 0 <= nj < m) or board[ni][nj] == 'D':
                    ni -= di
                    nj -= dj
                    break
                    
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == -1:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1        

    return -1
    
    
def solution(board):
    n, m = len(board), len(board[0])
    si, sj = 0, 0
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                si, sj = i, j
                
    return bfs(si, sj, board)