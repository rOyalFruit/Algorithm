def recursive(n):
    if n == 1:
        return ['*']

    size = n // 3
    smaller_pattern = recursive(size)
    new_pattern = []

    for line in smaller_pattern:
        new_pattern.append(line * 3)

    for line in smaller_pattern:
        new_pattern.append(line + ' ' * size + line)

    for line in smaller_pattern:
        new_pattern.append(line * 3)

    return new_pattern


n = int(input())
result = recursive(n)
print('\n'.join(result))
