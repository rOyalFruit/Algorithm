def solution(storey):
    answer = 0
    while storey > 0:
        remainder = storey % 10
        storey //= 10
        
        # 5보다 큰 경우 올림, 5인 경우는 다음 자릿수에 따라 결정
        if remainder > 5 or (remainder == 5 and storey % 10 >= 5):
            answer += 10 - remainder
            storey += 1
        else: 
            answer += remainder
            
    return answer
