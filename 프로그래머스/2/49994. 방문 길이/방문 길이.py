def solution(dirs):
    answer = 0
    ci, cj = 0, 0
    d = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}
    path = []
    
    for dir in dirs:
        di, dj = d[dir]
        ni, nj = ci + di, cj + dj
        
        if -5 <= ni <= 5 and -5 <= nj <= 5:
            if (ci, cj, ni, nj) not in path and (ni, nj, ci, cj) not in path:
                path.append((ci, cj, ni, nj))
                path.append((ni, nj, ci, cj))
                answer += 1
            ci, cj = ni, nj
            
    return answer