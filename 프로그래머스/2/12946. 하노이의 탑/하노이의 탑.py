def solution(n):
    def recursive(num_disk, start, via, end):
        if num_disk == 1:
            answer.append([start, end])
            return
        
        recursive(num_disk - 1, start, end, via)
        answer.append([start, end])
        recursive(num_disk - 1, via, start, end)
        
        
    answer = []
    recursive(n, 1, 2, 3)
    
    return answer
