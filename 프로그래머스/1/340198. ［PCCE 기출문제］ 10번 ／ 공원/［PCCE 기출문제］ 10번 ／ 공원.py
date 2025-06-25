def solution(mats, park):
    n, m = len(park), len(park[0])
    mats.sort(reverse=True) 
    
    for mat in mats:
        for i in range(n - mat + 1): 
            for j in range(m - mat + 1):
                if park[i][j] != "-1":
                    continue
                
                if all(park[k][l] == "-1" for k in range(i, i + mat) for l in range(j, j + mat)):
                    return mat
    return -1
