def recursive(n, k, start, via, end):
    if n == 1:
        print(start, end)
        return

    pivot = 2 ** (n-1)
    if k < pivot:
        recursive(n - 1, k, start, end, via)
    elif k == pivot:
        print(start, end)
        return
    else:
        recursive(n - 1, k - pivot, via, start, end)


n, k = map(int, input().split(" "))
recursive(n, k, 1, 2, 3)

# n = 3일 때 이동 과정
# 1, 3 ┐ k가 전반부에 속할 때
# 1, 2 │ n-1개의 원반을 start -> via로 옮기는 과정 탐색
# 3, 2 ┘
# 1, 3 - pivot n번 원반을 start -> end로 옮김 (정답)
# 2, 1 ┐ k가 후반부에 속할 때
# 2, 3 │ n-1개의 원반을 via -> end로 옮기는 과정 탐색
# 1, 3 ┘ 이미 pivot 만큼 이동했으므로 k 값을 조정
