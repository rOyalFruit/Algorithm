def solution(s):
    s = list(map(int, s.split(" ")))
    # return " ".join(map(str, [min(s), max(s)]))
    return f"{min(s)} {max(s)}"
