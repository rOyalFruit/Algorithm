def solution(s):
    answer = []
    parts = s[2:-2].split('},{')
    sets = sorted([set(map(int, p.split(','))) for p in parts], key=len)
    previous_set = set() 
    
    for current_set in sets:
        new_element = list(current_set - previous_set)[0]
        answer.append(new_element)
        previous_set = current_set 
        
    return answer