from collections import defaultdict, deque


def bfs(n, start, graph):
    q = deque([start])
    visited = [False] * (n+1)
    visited[start] = True
    
    while q:
        cur = q.popleft()
        
        for node in graph[cur]:
            if not visited[node]:
                q.append(node)
                visited[node] = True
                
    return sum(visited) - 1


def solution(n, results):
    answer = 0
    win_graph = defaultdict(list)
    lose_graph = defaultdict(list)
    
    for i, j in results:
        win_graph[i].append(j)
        lose_graph[j].append(i)

    for i in range(1, n+1):
        win_cnt = bfs(n, i, win_graph)
        lose_cnt = bfs(n, i, lose_graph)
        if win_cnt + lose_cnt == n - 1:
            answer += 1
            
    return answer