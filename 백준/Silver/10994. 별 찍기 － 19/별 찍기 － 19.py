def recursive(n):
    if n == 1:
        return ["*"]

    smaller_pattern = recursive(n - 1)
    new_pattern = []
    size = 4 * n - 3

    new_pattern.append("*" * size)
    new_pattern.append("*" + ' ' * (size - 2) + "*")
    for pattern in smaller_pattern:
        new_pattern.append("*" + ' ' + pattern + ' ' + "*")
    new_pattern.append("*" + ' ' * (size - 2) + "*")
    new_pattern.append("*" * size)

    return new_pattern


n = int(input())
result = recursive(n)
print("\n".join(result))
