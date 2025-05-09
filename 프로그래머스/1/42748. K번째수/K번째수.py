def solution(array, commands):
    answer = []
    for cmd in commands:
        i, j, k = cmd
        value = sorted(array[i-1:j])[k-1]
        answer.append(value)
    return answer