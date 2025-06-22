from collections import defaultdict, deque


def bfs(info, tree):
    max_sheep = 0
    q = deque([(0, 0, [0])])  # 양 수, 늑대 수, 후보 노드 리스트, 방문 집합

    while q:
        sheep, wolf, candidates = q.popleft()

        for i, node in enumerate(candidates):
            new_sheep, new_wolf = sheep, wolf
            
            if info[node] == 0:
                new_sheep += 1
            else:
                new_wolf += 1

            if new_wolf >= new_sheep:
                continue

            max_sheep = max(max_sheep, new_sheep)
            new_candidates = candidates[:i] + candidates[i+1:] + tree[node]
            q.append((new_sheep, new_wolf, new_candidates))

    return max_sheep


def solution(info, edges):
    tree = defaultdict(list)
    
    for p, c in edges:
        tree[p].append(c)

    return bfs(info, tree)
