def solution(dirs):
    ci, cj = 0, 0
    d = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}
    path = set()
    
    for dir in dirs:
        di, dj = d[dir]
        ni, nj = ci + di, cj + dj
        
        if -5 <= ni <= 5 and -5 <= nj <= 5:
            path.add((ci, cj, ni, nj))
            path.add((ni, nj, ci, cj))
            ci, cj = ni, nj
            
    return len(path) // 2