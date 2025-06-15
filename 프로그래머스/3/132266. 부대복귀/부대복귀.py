from collections import deque, defaultdict
  

def solution(n, roads, sources, destination):
    graph = defaultdict(list)
    
    for i, j in roads:
        graph[i].append(j)
        graph[j].append(i)
    
    visited = [-1] * (n+1)
    visited[destination] = 0
    q = deque([destination])
    
    while q:
        cur = q.popleft()
        
        for next in graph[cur]:
            if visited[next] == -1:
                visited[next] = visited[cur] + 1
                q.append(next)
                
    return [visited[source] if visited[source] != -1 else -1 for source in sources]