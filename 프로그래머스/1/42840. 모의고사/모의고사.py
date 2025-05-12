def solution(answers):
    answer = [0] * 4
    student_1 = [1, 2, 3, 4, 5]
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for idx, value in enumerate(answers):
        if student_1[idx % len(student_1)] == value:
            answer[1] += 1
        if student_2[idx % len(student_2)] == value:
            answer[2] += 1
        if student_3[idx % len(student_3)] == value:
            answer[3] += 1
    
    return [idx for idx, x in enumerate(answer) if x == max(answer)]