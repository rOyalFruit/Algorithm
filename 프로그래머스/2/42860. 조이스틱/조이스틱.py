def solution(name):
    vertical = 0
    horizontal = len(name) - 1  # 기본 최대 이동값
    
    # 1. 상하 이동 계산
    vertical = sum(min(ord(c) - ord('A'), ord('Z') - ord(c) + 1) for c in name)
    
    # 2. 좌우 이동 계산
    for i in range(len(name)):
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        horizontal = min(
            horizontal,                  # 기본 최대 이동값
            i * 2 + (len(name) - next),  # 앞으로 갔다가 뒤로
            i + (len(name) - next) * 2   # 뒤로 갔다가 앞으로
        )
    
    return vertical + horizontal