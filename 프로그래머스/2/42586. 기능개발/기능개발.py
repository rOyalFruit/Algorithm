import math


def solution(progresses, speeds):
    answer = []
    i = 0
    
    while i < len(progresses):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        count = 0
        for j in range(i, len(progresses)):

            if progresses[j] + speeds[j] * day < 100:
                break

            count += 1

        answer.append(count)
        i += count

    return answer