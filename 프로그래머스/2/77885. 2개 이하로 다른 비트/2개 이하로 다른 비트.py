def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num+1)
        else:
            # 홀수: 오른쪽부터 첫 번째 "01" 패턴을 "10"으로 변경
            bin_str = "0" + bin(num)[2:]
            
            # 오른쪽부터 "01" 패턴 찾기
            for i in range(len(bin_str) - 1, 0, -1):
                if bin_str[i-1:i+1] == "01":
                    # "01"을 "10"으로 변경
                    result = bin_str[:i-1] + "10" + bin_str[i+1:]
                    answer.append(int(result, 2))
                    break
            
    return answer
