def solution(players, m, k):
    answer = 0
    lst = [0] * 24 
    
    for i, player in enumerate(players):
        if (lst[i]+1) * m <= player: 
            n = (player // m) - lst[i]
            for j in range(i, i+k):
                if len(players) <= j:
                    break
                lst[j] += n
            answer += n
            
    return answer