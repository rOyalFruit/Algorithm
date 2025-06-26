def solution(absolutes, signs):
    return sum([absolutes[i] if sign else absolutes[i] * -1 for i, sign in enumerate(signs)])