def solution(numbers):
    answer = numbers
    num_dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, 
                "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    
    for k, v in num_dict.items():
        answer = answer.replace(k, str(v))
        
    return int(answer)