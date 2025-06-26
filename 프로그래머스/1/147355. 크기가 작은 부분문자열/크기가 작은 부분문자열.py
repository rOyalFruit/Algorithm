def solution(t, p):
    return sum([1 if int(t[i:i+len(p)]) <= int(p) else 0 for i in range(len(t)-len(p)+1)])