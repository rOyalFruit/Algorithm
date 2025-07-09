def solution(arr1, arr2):
    num_rows_arr1 = len(arr1)
    num_cols_arr2 = len(arr2[0])
    num_cols_arr1 = len(arr1[0])
    answer = [[0] * num_cols_arr2 for i in range(num_rows_arr1)]
    
    for i in range(num_rows_arr1):
        for j in range(num_cols_arr2):
            for k in range(num_cols_arr1):
                answer[i][j] += arr1[i][k] * arr2[k][j]
                
    return answer