from itertools import combinations


is_first_case = True
while True:
    line = list(map(int, input().split()))
    if line[0] == 0:
        break

    if not is_first_case:
        print()

    for combo in combinations(line[1:], 6):
        print(*combo)

    is_first_case = False
    