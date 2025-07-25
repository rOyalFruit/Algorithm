def recursive(n):
    if n == 1:
        return ["*"]

    if n == 2:
        return ["*****", "*    ", "* ***", "* * *", "* * *", "*   *", "*****"]

    smaller_pattern = recursive(n - 1)
    new_pattern = []

    new_pattern.append("*" * (4 * n -3))
    new_pattern.append("*" + ' ' * (4 * n - 4))
    for idx, pattern in enumerate(smaller_pattern):
        if idx == 0:
            new_pattern.append("* " + pattern + "**")
        else:
            new_pattern.append("* " +pattern + " *")
    new_pattern.append("*" + ' ' * (4 * n - 5) + "*")
    new_pattern.append("*" * (4 * n - 3))

    return new_pattern


n = int(input())
result = recursive(n)
for line in result:
    print(line.rstrip())