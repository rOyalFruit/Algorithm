from collections import Counter


def robot_path(route, points):
    r, c = points[route[0]-1]  # 시작 지점
    time = 0
    path = [(r, c, time)]  # 초기 위치

    # 경로 상의 다음 지점으로 이동
    for i in range(1, len(route)):
        next_r, next_c = points[route[i]-1]
        
        # r 이동
        while r != next_r:
            time += 1
            r += 1 if r < next_r else -1
            path.append((r, c, time))
        
        # c 이동
        while c != next_c:
            time += 1
            c += 1 if c < next_c else -1
            path.append((r, c, time))
    
    return path


def solution(points, routes):
    # 모든 로봇의 이동 경로 생성 [(r, c, time)]
    positions = []
    for route in routes:
        positions.extend(robot_path(route, points))
    
    # 충돌 횟수 계산
    answer = sum(1 for count in Counter(positions).values() if count >= 2)
    
    return answer