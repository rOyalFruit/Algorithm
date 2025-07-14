def solution(msg):
    # 1. 사전 초기화 (A-Z)
    answer = []
    dictionary = {chr(i):i-64 for i in range(65, 90+1)}
    next_idx = 27

    i = 0
    while i < len(msg):
        # 2. 현재 위치에서 가장 긴 단어(w) 찾기
        w = msg[i]
        while i + len(w) < len(msg) and w + msg[i + len(w)] in dictionary:
            w += msg[i + len(w)]

        # 3. w에 해당하는 색인 번호 출력
        answer.append(dictionary[w])

        # 4. 입력에서 처리한 w 제거 및 사전에 w+c 등록
        # 다음 글자(c)가 있는 경우에만 사전에 추가
        if i + len(w) < len(msg):
            c = msg[i + len(w)]
            dictionary[w + c] = next_idx
            next_idx += 1
        
        # 5. 현재 위치(i)를 w의 길이만큼 이동
        i += len(w)
        # print(f"{w=}, {c=}, {answer=}")
    return answer
