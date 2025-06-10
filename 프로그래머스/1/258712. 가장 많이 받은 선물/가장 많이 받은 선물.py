from itertools import combinations


def solution(friends, gifts):
    friend_index = {name: idx for idx, name in enumerate(friends)}
    n = len(friends)
    
    # 1. 선물 교환 기록 행렬 생성
    gift_matrix = [[0] * n for _ in range(n)]
    for gift in gifts:
        giver, receiver = gift.split()
        giver_idx = friend_index[giver]
        receiver_idx = friend_index[receiver]
        gift_matrix[giver_idx][receiver_idx] += 1
        
    # 2. 선물 지수 계산 (주고받은 선물 차이)
    gift_scores = [
        sum(given) - sum(received[me] for received in gift_matrix) for me, given in enumerate(gift_matrix)
    ]
    
    # 3. 다음 달 예상 선물 계산
    next_month = [0] * n
    
    for a, b in combinations(range(n), 2):
        a_to_b = gift_matrix[a][b]
        b_to_a = gift_matrix[b][a]
        
        if a_to_b > b_to_a:
            next_month[a] += 1
        elif a_to_b < b_to_a:
            next_month[b] += 1
        else:
            if gift_scores[a] > gift_scores[b]:
                next_month[a] += 1
            elif gift_scores[a] < gift_scores[b]:
                next_month[b] += 1
    
    return max(next_month)
