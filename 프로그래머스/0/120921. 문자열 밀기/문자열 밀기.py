def solution(A, B):
    word = A
    for i in range(len(A)):
        if word == B:
            return i
        word = word[-1] + word[:-1]
        
    return -1