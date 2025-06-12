def solution(myStr):
    s = myStr.replace('b', 'a').replace('c', 'a')
    s = [x for x in s.split('a') if x]
    
    return s if s else ["EMPTY"]