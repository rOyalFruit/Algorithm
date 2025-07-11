import heapq


def solution(n, works):
    answer = 0
    heap = []
    
    for work in works:
        heapq.heappush(heap, (-work, work))
    
    for i in range(n):
        num = heapq.heappop(heap)[1] - 1
        if num > 0:
            heapq.heappush(heap, (-num, num)) 
        else:
            heapq.heappush(heap, (0, 0)) 
    
    return sum([i[1] ** 2 for i in heap])