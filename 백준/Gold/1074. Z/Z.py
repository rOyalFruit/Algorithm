def solve(n, r, c):

    # Base Case: 가장 작은 단위(1x1)에 도달하면, 그 칸의 순서는 0이다.
    if n == 0:
        return 0

    half = 2**(n - 1)

    # 1. 1사분면 (왼쪽 위)에 속하는 경우
    if r < half and c < half:
        return solve(n - 1, r, c)
    # 2. 2사분면 (오른쪽 위)에 속하는 경우
    elif r < half <= c:
        # 1사분면의 크기만큼 오프셋 + 더 작은 문제의 결과
        # c 좌표는 작은 사각형 기준으로 다시 계산 (c - half)
        return (half * half) * 1 + solve(n - 1, r, c - half)
    # 3. 3사분면 (왼쪽 아래)에 속하는 경우
    elif r >= half > c:
        # 1, 2사분면의 크기만큼 오프셋 + 더 작은 문제의 결과
        # r 좌표는 작은 사각형 기준으로 다시 계산 (r - half)
        return (half * half) * 2 + solve(n - 1, r - half, c)
    # 4. 4사분면 (오른쪽 아래)에 속하는 경우
    else:
        # 1, 2, 3사분면의 크기만큼 오프셋 + 더 작은 문제의 결과
        # r, c 좌표 모두 작은 사각형 기준으로 다시 계산
        return (half * half) * 3 + solve(n - 1, r - half, c - half)


n, r, c = map(int, input().split(" "))
print(solve(n, r, c))
