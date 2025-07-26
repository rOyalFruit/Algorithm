def hanoi(n, start, via, end, result):
    if n <= 0:
        return

    hanoi(n - 1, start, end, via, result)
    result.append([start, end])
    hanoi(n - 1, via, start, end, result)
    return


def solve(n, start, via1, via2, end, result):
    if n <= 0:
        return

    if n == 1:
        result.append([start, end])
        return

    hanoi(n-2, start, via1, via2, result)
    result.append([start, via1])
    result.append([start, end])
    result.append([via1, end])
    solve(n-2, via2, start, via1, end, result)
    return


n = int(input())
result = []
solve(n, 'A', 'B', 'C', 'D', result)
print(len(result))
for i in result:
    print(*i)
