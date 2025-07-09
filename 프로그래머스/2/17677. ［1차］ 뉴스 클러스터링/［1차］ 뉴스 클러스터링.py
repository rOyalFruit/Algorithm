from collections import Counter


def solution(str1, str2):
    pairs1 = [str1[i:i+2].lower() for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    pairs2 = [str2[i:i+2].lower() for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]

    counter1 = Counter(pairs1)
    counter2 = Counter(pairs2)

    intersection_counter = counter1 & counter2  # 두 Counter의 공통 원소 중 더 작은 개수를 가지는 교집합
    union_counter = counter1 | counter2         # 두 Counter의 모든 원소 중 더 큰 개수를 가지는 합집합
    
    intersection_size = sum(intersection_counter.values())
    union_size = sum(union_counter.values())
    
    if union_size == 0:
        return 65536
    
    return int((intersection_size / union_size) * 65536)
