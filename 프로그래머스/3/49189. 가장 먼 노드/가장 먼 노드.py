from collections import defaultdict, deque


def bfs(n, start, graph):
    visited = [0] * (n+1)
    q = deque([start])
    visited[start] = 1
    
    while q:
        cur = q.popleft()
        for node in graph[cur]:
            if not visited[node]:
                q.append(node)
                visited[node] = visited[cur] + 1
    
    return visited


def solution(n, edge):
    graph = defaultdict(list)
    for k, v in edge:
        graph[k].append(v)
        graph[v].append(k)

    distance_list = bfs(n, 1, graph)
    max_dist = max(distance_list)
    
    return distance_list.count(max_dist)