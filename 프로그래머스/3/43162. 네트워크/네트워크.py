def bfs(i, n, computers, visited):
    if visited[i]:
        return 0
    
    q = [i]
    visited[i] = True
    
    while q:
        cur = q.pop(0)
        for j in range(n):
            if computers[cur][j] == 1 and not visited[j]:
                visited[j] = True
                q.append(j)
    
    return 1

def solution(n, computers):
    visited = [False for _ in range(n)]
    count = 0
    
    for i in range(n):
        count += bfs(i, n, computers, visited)
    
    return count
