from collections import defaultdict


def solution(record):
    answer = []
    enter_msg = "님이 들어왔습니다."
    leave_msg = "님이 나갔습니다."
    user = defaultdict(str)
    
    for r in record:
        info = r.split(" ")
        
        if info[0] == "Enter" or info[0] == "Change":
            user[info[1]] = info[2]
    
    for r in record:
        info = r.split(" ")
        
        if info[0] == "Enter":
            answer.append(user[info[1]] + enter_msg)
        elif info[0] == "Leave":
            answer.append(user[info[1]] + leave_msg)            
    
    return answer
