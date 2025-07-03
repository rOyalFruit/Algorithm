def solution(n, words):
    answer = [0, 0]
    used_words = set()
    prev = words[0][0]
    
    for i, word in enumerate(words):
        if word[0] == prev[-1] and word not in used_words :
            prev = word
            used_words .add(prev)
        else:
            answer[0] = i % n + 1
            answer[1] = i // n + 1
            break
            
    return answer