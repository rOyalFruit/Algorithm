import heapq


def solution(n, costs):
    answer = 0
    graph = [[] for _ in range(n)]
    for u, v, w in costs:
        graph[u].append((w, v))
        graph[v].append((w, u))
    
    visited = [False] * n
    heap = []
    heapq.heappush(heap, (0, 0))  # (가중치, 노드)
    
    while heap:
        weight, node = heapq.heappop(heap)
        if visited[node]:
            continue
        visited[node] = True
        answer += weight
        
        for next_weight, next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(heap, (next_weight, next_node))
    
    return answer