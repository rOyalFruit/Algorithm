def find_divisor_pairs(yellow):
    result = []
    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0:
            result.append((yellow//i, i))
    return result

def solution(brown, yellow):
    answer = []
    divisor_pairs = find_divisor_pairs(yellow)
    for width, height in divisor_pairs:
        if (width+2)*2 + height*2 == brown:
            return [width+2, height+2]
    return answer

