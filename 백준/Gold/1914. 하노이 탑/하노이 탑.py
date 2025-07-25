def recursive(n, start, via, end):
    if n == 1:
        print(*[start, end])
        return

    recursive(n - 1, start, end, via)
    print(*[start, end])
    recursive(n - 1, via, start, end)


n = int(input())
print(2**n - 1)
if n <= 20:
    recursive(n, 1, 2, 3)
