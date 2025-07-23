from collections import defaultdict


def solution(tickets):
    answer = []
    
    graph = defaultdict(list)
    for start, end in sorted(tickets, reverse=True):
        graph[start].append(end)
    
    stack = ["ICN"]
    path = []
    
    while stack:
        cur = stack[-1]
        
        if cur not in graph or not graph[cur]:
            path.append(stack.pop())
        else:
            stack.append(graph[cur].pop())
        
    return path[::-1]
