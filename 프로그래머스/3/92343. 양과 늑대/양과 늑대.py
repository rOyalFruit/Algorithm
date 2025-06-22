from collections import defaultdict


def dfs(info, tree, sheep, wolf, visited, candidates):
    max_sheep = sheep  # 현재 경로에서의 최대 양 수
    
    # 모든 후보 노드 탐색
    for i, node in enumerate(candidates):
        new_sheep, new_wolf = sheep, wolf
        
        # 현재 노드 유형 처리
        if info[node] == 0:
            new_sheep += 1
        else:
            new_wolf += 1
        
        # 늑대 >= 양인 경우 경로 차단
        if new_wolf >= new_sheep:
            continue
        
        # 새로운 상태 업데이트
        new_visited = visited | {node}
        new_candidates = candidates[:i] + candidates[i+1:] + [
            child for child in tree[node] 
            if child not in new_visited
        ]
        
        # 재귀 탐색 및 결과 비교
        result = dfs(info, tree, new_sheep, new_wolf, new_visited, new_candidates)
        max_sheep = max(max_sheep, result)
    
    return max_sheep


def solution(info, edges):
    # 트리 구조 생성
    tree = defaultdict(list)
    for parent, child in edges:
        tree[parent].append(child)
    
    # 초기값 설정 (루트 노드: 양 1마리)
    return dfs(info, tree, 1, 0, {0}, tree[0])
