from collections import defaultdict


def solution(array):
    answer = -1
    dic = defaultdict(int)
    
    for i in array:
        dic[i] += 1
    
    temp = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    if len(temp) > 1 and temp[0][1] == temp[1][1]:
        answer = -1
    else:
        answer = temp[0][0]
        
    return answer