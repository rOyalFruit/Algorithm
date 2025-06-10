from collections import deque


def solution(cacheSize, cities):
    answer = 0
    q = deque()
    
    for city in cities:
        if city.lower() in q:
            q.append(city.lower())
            q.remove(city.lower())
            answer += 1
        else:
            if len(q) >= cacheSize:
                q.append(city.lower())
                q.popleft()
            else:
                q.append(city.lower())
            answer += 5
            
    return answer
