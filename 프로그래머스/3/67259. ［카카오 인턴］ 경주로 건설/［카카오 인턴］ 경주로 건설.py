import heapq


def solution(board):
    costs = [[[float('inf')] * 4 for _ in range(len(board))] for _ in range(len(board))]
    costs[0][0] = [0] * 4
    heap = [(0, 0, 0, -1)]  # 비용, i, j, 방향
    
    while heap:
        cur_cost, ci, cj, prev_dir = heapq.heappop(heap)
        
        # 현재 상태가 더 낮은 비용으로 이미 처리된 경우 스킵
        if prev_dir != -1 and cur_cost > costs[ci][cj][prev_dir]:
            continue
        
        for cur_dir, (di, dj) in enumerate(zip([1, -1, 0, 0], [0, 0, 1, -1])):
            ni = ci + di
            nj = cj + dj
            
            if 0 <= ni < len(board) and 0 <= nj < len(board) and board[ni][nj] == 0:
                next_cost = cur_cost + 100
                
                if prev_dir != -1 and prev_dir != cur_dir:
                    next_cost += 500
                
                if next_cost < costs[ni][nj][cur_dir]:
                    costs[ni][nj][cur_dir] = next_cost
                    heapq.heappush(heap, (next_cost, ni, nj, cur_dir))
                    
    return min(costs[-1][-1])
