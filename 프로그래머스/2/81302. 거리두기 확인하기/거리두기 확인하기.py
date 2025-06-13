from itertools import combinations


def is_violated(p1, p2, place):
    r1, c1 = p1
    r2, c2 = p2
    dist = abs(r1 - r2) + abs(c1 - c2) # 맨해튼 거리 계산
    
    if dist > 2:  # 거리가 2 초과면 거리두기 위반 아님
        return False
    if r1 == r2:  # 같은 행
        return place[r1][(c1 + c2) // 2] in ['O', 'P']
    if c1 == c2:  # 같은 열
        return place[(r1 + r2) // 2][c1] in ['O', 'P']
    return place[r1][c2] in ['O', 'P'] or place[r2][c1] in ['O', 'P']  # 대각선


def solution(places):
    answer = []
    for place in places:
        # 모든 사람(P)의 위치를 리스트로 저장
        people = [(i, j) for i in range(5) for j in range(5) if place[i][j] == 'P']
        
        # 모든 사람 쌍에 대해 거리두기 위반 여부 확인
        for p1, p2 in combinations(people, 2):
            if is_violated(p1, p2, place):
                answer.append(0)
                break
        else:
            answer.append(1)
            
    return answer