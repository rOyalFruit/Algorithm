from collections import Counter


def solution(want, number, discount):
    answer = 0
    n = len(discount)
    m = sum(number)
    want_dict = dict(zip(want, number))

    for i in range(n-m+1):
        discount_count = Counter(discount[i:i+m])
        
        if want_dict == discount_count:
            answer += 1
        
    return answer