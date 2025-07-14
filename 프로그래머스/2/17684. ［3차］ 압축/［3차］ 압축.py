from collections import defaultdict


def solution(msg):
    answer = []
    idx = 1
    d = defaultdict(int)
    for i in range(65, 90+1):
        d[chr(i)] = idx
        idx += 1
    
    word = ""
    prev = msg[0]
    for i in range(1, len(msg)):
        word = prev + msg[i]
        if word in d:
            prev = word
            continue
        answer.append(d[prev])
        prev = msg[i]
        d[word] = idx
        idx += 1
    answer.append(d[prev])
    
    return answer