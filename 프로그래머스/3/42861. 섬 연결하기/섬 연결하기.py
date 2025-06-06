import heapq


def solution(n, costs):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [False] * n
    heap = []
    heapq.heappush(heap, (0, 0))
    
    for u, v, w in costs:
        graph[u].append((w, v))
        graph[v].append((w, u))
        
    while heap:
        weight, node = heapq.heappop(heap)
        
        if not visited[node]:
            answer += weight
            visited[node] = True
        
        for next_weight, next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(heap, (next_weight, next_node))
        
    return answer