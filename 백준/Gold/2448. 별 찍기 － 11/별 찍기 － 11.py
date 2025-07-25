def recursive(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']

    half = n // 2
    smaller_pattern = recursive(half)
    new_pattern = []

    # 3. 상단부 만들기: 작은 패턴을 가운데에 배치
    # 각 라인의 좌우에 'n/2' 만큼 공백 추가
    for line in smaller_pattern:
        new_pattern.append(' ' * half + line + ' ' * half)

    # 4. 하단부 만들기: 작은 패턴 두 개를 나란히 배치
    # 각 라인을 가져와서 ' ' 하나를 사이에 두고 이어붙임
    for line in smaller_pattern:
        new_pattern.append(line + ' ' + line)

    return new_pattern


n = int(input())
result = recursive(n)
print('\n'.join(result))
