def solution(myString, pat):
    n, m = len(myString), len(pat)
    for i in range(n, m-2, -1):
        if myString[i-m:i] == pat:
            return myString[:i]
    return None