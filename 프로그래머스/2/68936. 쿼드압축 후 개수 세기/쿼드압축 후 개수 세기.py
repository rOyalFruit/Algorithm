def solution(arr):
    def recursive(row, col, size):
        nonlocal answer
        start_val = arr[row][col]
        
        is_valid = True
        for r in range(row, row+size):
            for c in range(col, col+size):
                if arr[r][c] != start_val:
                    is_valid = False
                    break
            if not is_valid:
                break
        
        if is_valid:
            answer[start_val] += 1
            return
        
        half = size // 2
        recursive(row, col, half)
        recursive(row, col+half, half)
        recursive(row+half, col, half)
        recursive(row+half, col+half, half)
        
    
    answer = [0, 0]
    recursive(0, 0, len(arr))
    
    return answer