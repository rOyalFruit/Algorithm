from collections import Counter

def func(s):
    result = []
    s = s.lower()
    
    for i in range(len(s)-1):
        if 97 <= ord(s[i]) <= 122 and 97 <= ord(s[i+1]) <= 122:
            result.append(s[i:i+2])
    
    return result


def solution(str1, str2):
    lst1 = func(str1)
    lst2 = func(str2)

    union = set(lst1) | set(lst2)
    intersection = set(lst1) & set(lst2)
    
    lst1_counter = Counter(lst1)
    lst2_counter = Counter(lst2)

    u = []
    i = []
    for key in union:
        for _ in range(max(lst1_counter[key], lst2_counter[key])):
            u.append(key)
    
    for key in intersection:
        for _ in range(min(lst1_counter[key], lst2_counter[key])):
            i.append(key)
            
    return int(len(i) / len(u) * 65536) if len(u) != 0 else 65536
