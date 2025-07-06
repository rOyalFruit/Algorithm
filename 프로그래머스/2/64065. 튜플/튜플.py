def parse_string(s):
    content = s[2:-2]             # "2},{2,1},{2,1,3},{2,1,3,4"
    parts = content.split('},{')  # ['2', '2,1', '2,1,3', '2,1,3,4']
    result = []
    
    for part in parts:
        # '2,1' -> ['2', '1'] -> [2, 1]
        numbers = [int(num) for num in part.split(',')]
        result.append(numbers)
        
    return result


def solution(s):
    content = parse_string(s)
    content.sort(key=len)
    nums_set = set()
    answer = []
    
    for lst in content:
        for num in lst:
            if num in nums_set:
                continue
                
            nums_set.add(num)
            answer.append(num)
            
    return answer