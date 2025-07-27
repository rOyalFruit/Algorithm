def is_correct_string(s):
    """문자열 s가 '올바른 괄호 문자열'인지 확인하는 헬퍼 함수"""
    count = 0
    for char in s:
        if char == '(':
            count += 1
        else:
            count -= 1
        
        if count < 0:
            return False
            
    return count == 0


def solution(p):
    # 1. Base Case: 입력이 빈 문자열인 경우
    if not p:
        return ""

    # 2. 'u'와 'v' 분리
    balance = 0
    for i, char in enumerate(p):
        if char == '(':
            balance += 1
        else:
            balance -= 1
        
        if balance == 0:
            u = p[:i+1]
            v = p[i+1:]
            break

    # 3. 'u'가 올바른 괄호 문자열인 경우
    if is_correct_string(u):
        # v에 대해 재귀 호출하고 u에 이어 붙여 반환
        return u + solution(v)
    # 4. 'u'가 올바른 괄호 문자열이 아닌 경우
    else:
        # 4-1. ~ 4-3. 구현
        new_str = "(" + solution(v) + ")"
        
        # 4-4. u의 양 끝을 제거하고 괄호 방향을 뒤집어 붙임
        reversed_u = "".join([')' if char == '(' else '(' for char in u[1:-1]])
        new_str += reversed_u
        
        return new_str
