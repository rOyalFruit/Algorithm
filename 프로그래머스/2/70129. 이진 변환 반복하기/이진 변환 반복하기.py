def solution(s):
    count_0 = 0
    count_total = 0
    
    while s != "1":
        new_s = ""
        
        for c in s:
            if c == "1":
                new_s += c
            else:
                count_0 += 1
        
        s = bin(len(new_s))[2:]
        count_total += 1
        
    return [count_total, count_0]