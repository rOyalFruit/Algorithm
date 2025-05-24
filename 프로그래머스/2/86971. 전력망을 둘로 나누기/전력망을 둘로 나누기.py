def bfs(start, wires, excluded_edge):
    visited = [False] * (len(wires) + 1)
    queue = [start]
    visited[start] = True
    
    while queue:
        cur = queue.pop(0)
        
        for wire in wires[cur]:
            if (cur, wire) == excluded_edge or (wire, cur) == excluded_edge:
                continue
            
            if not visited[wire]:
                queue.append(wire)
                visited[wire] = True

    return sum(visited)


def solution(n, wires):
    answer = n
    wires_dict = {i: [] for i in range(1, n+1)}
    
    for s, e in wires:
        wires_dict[s].append(e)
        wires_dict[e].append(s)
    
    for s, e in wires:
        size1 = bfs(s, wires_dict, (s, e))
        size2 = n - size1
        answer = min(answer, abs(size1-size2))
        
    return answer