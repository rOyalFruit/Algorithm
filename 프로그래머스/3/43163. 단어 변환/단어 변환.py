def is_one_char_diff(word1, word2):
    if len(word1) != len(word2):
        return False
    
    diff_count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            diff_count += 1
            if diff_count > 1:
                return False
            
    return diff_count == 1
    

def solution(begin, target, words):
    visited = {word: False for word in words}
    q = [(begin, 0)]  # (단어, 변환 횟수) 쌍으로 저장
    
    while q:
        cur_word, cur_count = q.pop(0)
        
        if cur_word == target:
            return cur_count
        
        for word in words:
            if not visited.get(word) and is_one_char_diff(cur_word, word):
                q.append((word, cur_count + 1))
                visited[word] = True
        
    return 0