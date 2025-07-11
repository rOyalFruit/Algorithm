import heapq


def solution(n, works):
    if sum(works) < n:
        return 0
    
    heapq.heapify(works := [-i for i in works])
    
    for i in range(n):
        heapq.heappush(works, heapq.heappop(works)+1)
        
    return sum([i*i for i in works])