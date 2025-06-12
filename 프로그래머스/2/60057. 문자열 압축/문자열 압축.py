def solution(s):
    answer = len(s)
    
    for n in range(1, len(s) // 2 + 1):  
        str_list = [s[i:i+n] for i in range(0, len(s), n)]  # 문자열 n개씩 자르기
        
        count = 0
        lst = []
        result = ''
        prev = str_list[0]
        
        for string in str_list:
            if string == prev:
                count += 1
                lst.append(string)
            else:
                result += prev if count == 1 else str(len(lst)) + prev
                lst = [string]
                count = 1
                prev = string
        
        if lst:
            result += prev if count == 1 else str(len(lst)) + prev
        
        answer = min(answer, len(result))
        
    return answer