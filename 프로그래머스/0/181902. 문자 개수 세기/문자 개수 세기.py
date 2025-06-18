def solution(my_string):
    c_dict = {chr(c): 0 for c in range(ord('A'), ord('Z')+1)}
    c_dict.update({chr(c): 0 for c in range(ord('a'), ord('z')+1)})
    
    for c in my_string:
        c_dict[c] += 1
        
    return list(c_dict.values())