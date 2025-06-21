from collections import defaultdict


def dfs(info, tree, sheep, wolf, visited, candidates, max_sheep):
    max_sheep[0] = max(max_sheep[0], sheep)
    
    for i, node in enumerate(candidates):
        new_sheep, new_wolf = sheep, wolf
        if info[node] == 0:
            new_sheep += 1
        else:
            new_wolf += 1
        
        if new_wolf >= new_sheep:
            continue
        
        new_visited = visited | {node}
        new_candidates = candidates[:i] + candidates[i+1:] + tree[node]
        dfs(info, tree, new_sheep, new_wolf, new_visited, new_candidates, max_sheep)

def solution(info, edges):
    tree = defaultdict(list)
    for s, e in edges:
        tree[s].append(e)
        
    max_sheep = [0]
    dfs(info, tree, 1, 0, {0}, tree[0], max_sheep)
    return max_sheep[0]
