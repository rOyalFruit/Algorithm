def solution(triangle):
    n = len(triangle)
    answer = [[0] * i for i in range(1, len(triangle))]
    answer.append(triangle[n-1])
    
    for i in range(n-2, -1, -1):
        for j, num in enumerate(triangle[i]):
            answer[i][j] = max(num + answer[i+1][j], num + answer[i+1][j+1])
            
    return answer[0][0]