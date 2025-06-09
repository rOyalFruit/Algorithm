import heapq


def solution(jobs):
    jobs.sort()
    time, total, idx, count = 0, 0, 0, 0
    heap = []
    n = len(jobs)
    
    while count < n:
        while idx < n and jobs[idx][0] <= time:
            heapq.heappush(heap, (jobs[idx][1], jobs[idx][0]))
            idx += 1
        
        if heap:
            work_time, request_time = heapq.heappop(heap)
            time += work_time
            total += (time - request_time)
            count += 1
        else:
            time = jobs[idx][0]
            
    return total // n