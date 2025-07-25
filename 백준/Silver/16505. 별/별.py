def recursive(n):
    if n == 0:
        return ["*"]

    smaller_pattern = recursive(n - 1)
    new_pattern = []

    for pattern in smaller_pattern:
        new_pattern.append(pattern * 2)

    for pattern in smaller_pattern:
        new_pattern.append(pattern + ' ' * len(pattern))

    return new_pattern


n = int(input())
result = recursive(n)
for line in result:
    print(line.rstrip())
