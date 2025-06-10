def solution(friends, gifts):
    n = len(friends)
    friends_dict = {k:v for v, k in enumerate(friends)}
    gift_graph = [[0] * n for _ in range(n)]
    gift_score = [0] * n
    
    # 주고받은 선물
    for gift in gifts:
        sender, reciever = gift.split(" ")
        gift_graph[friends_dict[sender]][friends_dict[reciever]] += 1
    
    # 선물 지수 구하기
    for i in range(n):
        gift_score[i] = sum(gift_graph[i]) - sum(recieved[i] for recieved in gift_graph)
        
    # 다음 달에 받을 선물 수 구하기
    temp = [0] * n
    visited = [[False] * n for _ in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                continue
                
            if not visited[i][j] and not visited[j][i]:
                if gift_graph[i][j] > gift_graph[j][i]:
                    temp[i] += 1
                elif gift_graph[i][j] < gift_graph[j][i]:
                    temp[j] += 1
                else:
                    if gift_score[i] > gift_score[j]:
                        temp[i] += 1
                    elif gift_score[i] < gift_score[j]:
                        temp[j] += 1
                
                visited[i][j] = True
                visited[j][i] = True
                    
    # 가장 많은 선물을 받는 친구가 받을 선물의 수 구하기
    return max(temp)