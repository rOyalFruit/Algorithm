from collections import deque


def build_tree(edges, n):
    graph = [deque() for _ in range(n+1)]
    
    for u, v in edges:
        graph[u].append(v)
    
    for i in range(1, n+1):
        graph[i] = deque(sorted(graph[i]))
    
    return graph


def simulate_drops(graph, target):
    n = len(target)
    visit_count = [0] * (n+1)
    leaf_sequence = []
    
    while True:
        # 리프 노드까지 이동
        current = 1
        while graph[current]:
            next_node = graph[current].popleft()
            graph[current].append(next_node)
            current = next_node
        
        # 리프 노드 도착 처리
        visit_count[current] += 1
        leaf_sequence.append(current)
        
        # 불가능 조건 검사
        if visit_count[current] > target[current-1]:
            return None, None
        
        # 모든 리프 노드가 타겟 조건을 만족하는지 확인
        all_satisfied = all(
            visit_count[i] <= target[i-1] <= 3 * visit_count[i]
            for i in range(1, n+1) 
            if not graph[i]
        )
        
        if all_satisfied:
            break
            
    return leaf_sequence, visit_count


def assign_numbers(graph, visit_count, target):
    n = len(target)
    leaf_numbers = [[] for _ in range(n+1)]
    
    for i in range(1, n+1):
        if not graph[i]:  # 리프 노드만 처리
            cnt = visit_count[i]
            leaf_numbers[i] = [1] * cnt
            remaining = target[i-1] - cnt
            
            for j in range(len(leaf_numbers[i])):
                if remaining >= 2:
                    leaf_numbers[i][j] = 3
                    remaining -= 2
                elif remaining == 1:
                    leaf_numbers[i][j] = 2
                    remaining -= 1
                else:
                    break
                    
    return leaf_numbers


def generate_result(leaf_sequence, leaf_numbers):
    """리프 방문 순서에 따라 최종 결과 생성"""
    result = []
    for leaf in leaf_sequence:
        # 사전 순 최소 보장: 마지막 요소 사용
        result.append(leaf_numbers[leaf].pop())
    
    return result
    
    
def solution(edges, target):
    n = len(target)
    
    # Step 1: 트리 구조 생성
    graph = build_tree(edges, n)

    # Step 2: 최소 드롭 횟수 찾기
    leaf_sequence, visit_count = simulate_drops(graph, target)
    
    # Step 3: 불가능한 경우 처리
    if leaf_sequence is None:
        return [-1]
    
    # Stpe 4: 각 리프 노드별 숫자 배분 계획 수립
    leaf_numbers = assign_numbers(graph, visit_count, target)
    
    # Step 5: 최종 결과 생성
    result = generate_result(leaf_sequence, leaf_numbers)
    
    return result