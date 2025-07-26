def recursive(i, j, n):

    color = board[i][j]
    for y in range(i, i+n):
        for x in range(j, j+n):
            if board[y][x] != color:
                half = n // 2

                res1 = recursive(i, j, half)
                res2 = recursive(i, j + half, half)
                res3 = recursive(i + half, j, half)
                res4 = recursive(i + half, j + half, half)

                white_sum = res1[0] + res2[0] + res3[0] + res4[0]
                blue_sum = res1[1] + res2[1] + res3[1] + res4[1]
                return [white_sum, blue_sum]

    return [1, 0] if color == '0' else [0, 1]


n = int(input())
board = [input().split(" ") for i in range(n)]
white_count, blue_count = recursive(0, 0, n)
print(white_count)
print(blue_count)
