def recursive(n, start, via, end):
    global result
    if n == 1:
        result.append([start, end])
        return

    recursive(n - 1, start, end, via)
    result.append([start, end])
    recursive(n - 1, via, start, end)


n = int(input())
result = []
recursive(n, 1, 2, 3)

print(len(result))
for i in result:
    print(*i)
