from itertools import combinations


def solution(places):
    answer = []
    for place in places:
        p_location = []
        for i in range(len(place)):
            for j in range(len(place[i])):
                if place[i][j] == 'P':
                    p_location.append((i, j))
        
        combi = combinations(p_location, 2)
        
        place_result = 1
        for p1, p2 in combi:
            if abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) <= 2: # 맨해튼 거리가 2 이하면 파티션이 있는지 검사
                if p1[0] == p2[0]:  # 같은 행에 있는 경우
                    if place[p1[0]][(p1[1] + p2[1]) // 2] in ['O', 'P']:
                        place_result = 0
                        break
                elif p1[1] == p2[1]:  # 같은 열에 있는 경우
                    if place[(p1[0] + p2[0]) // 2][p1[1]] in ['O', 'P']:
                        place_result = 0
                        break
                else:  # 대각선 방향에 있는 경우
                    if place[p1[0]][p2[1]] in ['O', 'P'] or place[p2[0]][p1[1]] in ['O', 'P']:
                        place_result = 0
                        break
        
        answer.append(place_result)
        
    return answer