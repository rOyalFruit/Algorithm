import heapq


def solution(operations):
    heap = []
    heapq.heapify(heap)
    
    for op in operations:
        cmd, num = op.split(" ")
        num = int(num)
        
        if cmd == "I":
            heapq.heappush(heap, num)
            
        if cmd == "D":
            if len(heap) == 0:
                continue
            if num == 1:
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
            if num == -1:
                heapq.heapify(heap)
                heapq.heappop(heap)
        
    return [0, 0] if len(heap) == 0 else [max(heap), heapq.heappop(heap)]